# 🚀 Agentic AI-Based AWS IAM Automation with RAG, GraphRAG & Human-in-the-Loop Governance

An AI-powered AWS automation system that combines **Retrieval-Augmented Generation (RAG)**, **GraphRAG**, **tool-integrated agents**, and **human-in-the-loop approval workflows** to safely automate AWS IAM troubleshooting and remediation actions.

The system retrieves contextual knowledge from AWS IAM documentation, reasons over it using an LLM agent, and executes remediation workflows while enforcing **approval gating for high-impact operations**.

---

# 📌 Overview

This project implements a **production-style Agentic AI system** designed to simulate enterprise-grade cloud automation and change management.

Key capabilities:

- Retrieves contextual knowledge from AWS IAM documentation using **Traditional RAG + GraphRAG**
- Uses an **LLM-powered agent** to reason over retrieved context and determine remediation actions
- Classifies AWS operations as **reversible/irreversible** and **high/low impact**
- Enforces **human approval gating for high-impact actions**
- Maintains **persistent state and traceable execution workflows**

This approach ensures **safe, auditable, and controlled AI-driven cloud automation**.

---

# 🧠 System Architecture

User (Streamlit UI) -> LangGraph Agent -> Hybrid Retrival Layer (Graph RAG + Vector RAG) -> AWS Action Tool -> High-Impact Detection -> Interrupt -> Human Approval -> Resume Execution

---

# ⚙️ Core Components

### 🤖 Agent Layer
- **LangGraph-based Agent**
- Performs reasoning over retrieved context
- Decides remediation actions and tool usage

### 📚 Knowledge Retrieval Layer

The system uses **Hybrid Knowledge Retrieval**:

#### Traditional RAG
- Embedding-based semantic search
- Vector similarity retrieval
- Metadata filtering

#### GraphRAG
- Builds a knowledge graph from AWS IAM documentation
- Captures relationships between entities such as:
  - IAM Roles
  - Policies
  - Permissions
  - Services
- Enables **relationship-aware retrieval** for deeper contextual reasoning

This hybrid approach improves **retrieval accuracy and reasoning depth**.

<img width="690" height="727" alt="Screenshot 2026-03-08 205800" src="https://github.com/user-attachments/assets/6570a470-ea2b-4d7e-8b1d-a159227997a6" />

<img width="1170" height="785" alt="Screenshot 2026-03-07 173423" src="https://github.com/user-attachments/assets/c0141a5d-f7a4-4822-9dd9-ba7bbfdca3ff" />


---

### 🛠 AWS Action Tool Layer

Handles automated remediation actions.

Capabilities:

- Executes AWS-related configuration actions
- Classifies actions based on:
  - **Reversible / Irreversible**
  - **Low Impact / High Impact**
- Prevents unsafe execution of irreversible operations.

---

### 🧑‍⚖️ Human-in-the-Loop Governance

High-impact actions require **manual approval** before execution.

Workflow:

1. Agent proposes an action.
2. Action is classified for impact.
3. If **high impact**, execution pauses using interrupt().
4. User approves or rejects the action via the UI.
5. Workflow resumes safely.

This ensures **enterprise-grade governance and operational safety**.

---

# 🔄 Human-in-the-Loop Workflow

1. User submits an AWS troubleshooting query.
2. Agent retrieves relevant IAM documentation using **RAG + GraphRAG**.
3. Agent analyzes context and determines the required AWS action.
4. Tool classifies the action:
   - Reversible
   - Irreversible
   - High Impact
   - Low Impact
5. If action is **High Impact** or **irreversible**:
   - Execution pauses using interrupt
   - UI requests user approval
6. Agent resumes execution after approval.

---

# 🎯 Key Features

- Hybrid **RAG + GraphRAG knowledge retrieval**
- **Agentic AI reasoning workflows**
- **Tool-integrated AWS automation**
- **Human-in-the-loop approval gating**
- **Safe cloud automation**
- **Enterprise-style governance simulation**

---

# 📈 Use Cases

This system can be extended to support:

- Cloud **incident remediation**
- Automated **DevOps troubleshooting**
- **Infrastructure governance**
- Secure **AI-assisted cloud operations**

---

## Screenshots

<img width="1919" height="925" alt="image" src="https://github.com/user-attachments/assets/19a114c4-cb23-4c38-836f-2151ef55e59b" />

<img width="1919" height="927" alt="image" src="https://github.com/user-attachments/assets/9ef9cab5-96ea-498e-850b-3ce56160d917" />

<img width="1919" height="924" alt="image" src="https://github.com/user-attachments/assets/4365f981-f53d-45fd-954a-8cf0a8a98f28" />

<img width="1918" height="922" alt="image" src="https://github.com/user-attachments/assets/0315e02a-7016-4be2-866d-9d55c792cf39" />

<img width="1919" height="770" alt="image" src="https://github.com/user-attachments/assets/8bcd11dc-b615-45b0-bf4a-1672b6251c7b" />

<img width="1919" height="729" alt="image" src="https://github.com/user-attachments/assets/915ea48d-4304-4534-bd7d-988d91dbad40" />

<img width="1919" height="773" alt="image" src="https://github.com/user-attachments/assets/e3e4866e-cb80-4d25-8ab4-49643e9fe50b" />

<img width="1919" height="757" alt="image" src="https://github.com/user-attachments/assets/391b99e8-99e9-4c16-9a29-cb8533b452d7" />

<img width="1919" height="764" alt="image" src="https://github.com/user-attachments/assets/79a4ccbd-a89f-430e-b491-9e104d45c182" />

<img width="1919" height="733" alt="image" src="https://github.com/user-attachments/assets/fb74ce0a-4d61-4b66-b796-53a6561d2825" />

--- 

# 🧑‍💻 Author

**Iniyan S**  
AI Engineer  

- GitHub: https://github.com/Iniyan307  
- LinkedIn: https://linkedin.com/in/iniyan-307-s  

---
