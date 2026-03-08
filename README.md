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
3. If **high impact**, execution pauses using `interrupt()`.
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

5. If action is **High Impact**:
   - Execution pauses using `interrupt()`
   - UI requests user approval
6. Agent resumes execution after approval.

---

# 🛠 Tech Stack

**Programming**
- Python

**Agent Framework**
- LangGraph
- LangChain

**Retrieval**
- Vector RAG
- GraphRAG

**Databases**
- Vector Database (Embeddings)
- Graph Knowledge Representation

**Frontend**
- Streamlit

**AI Concepts**
- Agentic AI
- Retrieval-Augmented Generation
- Tool-Calling Agents
- Human-in-the-loop AI

---

# 📂 Project Structure

<img width="387" height="681" alt="image" src="https://github.com/user-attachments/assets/4a2657c7-1278-42f4-925f-12c1bf272ac0" />

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

# 🧑‍💻 Author

**Iniyan S**  
AI Engineer  

- GitHub: https://github.com/Iniyan307  
- LinkedIn: https://linkedin.com/in/iniyan-307-s  

---


# 🚀 Agentic AI-Based AWS IAM Automation with Hybrid RAG & Human-in-the-Loop Governance

An AI-powered AWS automation system that combines **Retrieval-Augmented Generation (RAG)**, **tool-integrated agents**, and **human-in-the-loop approval workflows** to safely automate AWS IAM troubleshooting and remediation actions.

---

## 📌 Overview

This project implements a production-style **Agentic AI system** that:

- Retrieves contextual knowledge from AWS IAM documentation using RAG
- Decides remediation steps using LLM-based reasoning
- Classifies actions as reversible / irreversible and high / low impact
- Enforces approval gating for high-impact production actions
- Maintains persistent conversational state and audit-ready execution flow

The system is designed to simulate enterprise-grade cloud change management automation.

---

## 🧠 Architecture

User (Streamlit UI) -> LangGraph Agent -> Hybrid RAG (Graph RAG + Traditional RAG) -> AWS Action Tool -> High-Impact Detection -> Interrupt -> Human Approval -> Resume Execution

---

## ⚙️ Core Components

- **LLM-based Agent** for reasoning and decision-making  
- **RAG pipeline** over AWS IAM User Guides  
- **Hybrid retrieval** (vector similarity + metadata filtering)  
- **Tool-integrated AWS action execution layer**  
- **Human-in-the-loop approval system using LangGraph interrupts**  
- **Persistent state management via checkpointing**

---

## 🛠 Tech Stack

- Python  
- LangGraph  
- LangChain  
- Vector Database (for embeddings storage)  
- Streamlit  

---

## 🔄 Human-in-the-Loop Workflow

1. User submits AWS-related query.
2. Agent retrieves relevant IAM documentation via RAG.
3. Agent determines required AWS action.
4. Tool classifies action:
   - Reversible
   - High Impact
5. If High Impact:
   - Execution pauses using `interrupt()`
   - User approval is requested from UI
   - Workflow resumes only after approval
6. Action is executed or safely rejected.

This ensures **production-safe automation with governance controls**.

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
