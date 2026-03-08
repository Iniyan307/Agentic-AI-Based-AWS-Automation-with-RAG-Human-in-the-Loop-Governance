from langchain_core.documents import Document
from typing import List
import fitz  # PyMuPDF
from langchain_text_splitters import RecursiveCharacterTextSplitter


# --------------------------------------------------
# PDF SECTION CHUNKER
# --------------------------------------------------
class PDFSectionChunker:
    def __init__(
        self,
        chunk_size=1000,
        chunk_overlap=200,
        heading_min_size=14,
        heading_max_size=18,
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.heading_min_size = heading_min_size
        self.heading_max_size = heading_max_size

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", ". "]
        )

    def _flush_buffer(self, text: str, metadata: dict, documents: List[Document]):
        """Split buffered text and attach metadata to every chunk"""
        for chunk in self.splitter.split_text(text):
            header = ""

            if metadata.get("section"):
                header += f"Section: {metadata['section']}\n"
            if metadata.get("subsection"):
                header += f"Subsection: {metadata['subsection']}\n"

            if header:
                header += "\n"

            documents.append(
                Document(
                    page_content=header + chunk,
                    metadata=metadata.copy()
                )
            )

    def process_pdf(self, pdf_path: str) -> List[Document]:
        doc = fitz.open(pdf_path)

        pages = []
        all_heading_sizes = set()

        # ---- Extract headings + text blocks ----
        for page_no, page in enumerate(doc, 1):
            headings = []
            blocks = []

            for block in page.get_text("dict")["blocks"]:
                if "lines" not in block:
                    continue

                block_text = []
                block_y = block["bbox"][1]

                for line in block["lines"]:
                    line_text = " ".join(
                        span["text"] for span in line["spans"]
                    ).strip()

                    if not line_text:
                        continue

                    sizes = [round(span["size"]) for span in line["spans"]]
                    max_size = max(sizes)

                    if self.heading_min_size <= max_size <= self.heading_max_size:
                        headings.append({
                            "text": line_text,
                            "size": max_size,
                            "y": line["bbox"][1]
                        })
                        all_heading_sizes.add(max_size)
                    else:
                        block_text.append(line_text)

                if block_text:
                    blocks.append({
                        "text": " ".join(block_text),
                        "y": block_y
                    })

            pages.append({
                "page": page_no,
                "headings": sorted(headings, key=lambda x: x["y"]),
                "blocks": sorted(blocks, key=lambda x: x["y"])
            })

        # ---- Detect heading hierarchy ----
        sizes = sorted(all_heading_sizes, reverse=True)
        h1_size = sizes[0] if len(sizes) > 0 else None
        h2_size = sizes[1] if len(sizes) > 1 else None

        # print("Detected heading sizes:", {"H1": h1_size, "H2": h2_size})

        # --------------------------------------------------
        # 3️⃣ Section-aware chunking
        # --------------------------------------------------
        documents = []
        current_h1, current_h2 = None, None
        section_buffer = ""

        for page in pages:
            heads = page["headings"]
            blocks = page["blocks"]
            head_idx = 0

            for block in blocks:
                # Update section on heading transition
                while head_idx < len(heads) and heads[head_idx]["y"] < block["y"]:
                    if section_buffer.strip():
                        self._flush_buffer(
                            section_buffer,
                            {
                                "page": page["page"],
                                "section": current_h1,
                                "subsection": current_h2,
                                "source": pdf_path
                            },
                            documents
                        )
                        section_buffer = ""

                    h = heads[head_idx]
                    if h["size"] == h1_size:
                        current_h1 = h["text"]
                        current_h2 = None
                    elif h["size"] == h2_size:
                        current_h2 = h["text"]

                    head_idx += 1

                # Always keep metadata updated
                section_meta = {
                    "page": page["page"],
                    "section": current_h1,
                    "subsection": current_h2,
                    "source": pdf_path
                }

                section_buffer += block["text"] + "\n\n"

                if len(section_buffer) >= self.chunk_size:
                    self._flush_buffer(section_buffer, section_meta, documents)
                    section_buffer = ""

        # Flush remaining text
        if section_buffer.strip():
            self._flush_buffer(
                section_buffer,
                {
                    "page": page["page"],
                    "section": current_h1,
                    "subsection": current_h2,
                    "source": pdf_path
                },
                documents
            )

        return documents
    
def clean_metadata(metadata: dict) -> dict:
    return {k: v for k, v in metadata.items() if v is not None}


# ---- MAIN function ----
def chunker(file_path):
    chunker = PDFSectionChunker(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = chunker.process_pdf(file_path)

    print("Total chunks:", len(chunks))
    # for chunk in chunks:
    #     print(chunk, "________________________________")
    # print(chunks[0].page_content)
    return chunks

if __name__ == "__main__":
    chunker("data\pdf\AWSiamUserGuide_modified.pdf")