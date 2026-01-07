# Agent Framework  
### PDF Analyzer • Resume Analyzer • Q&A Agent (FastAPI)

A modular **Agentic AI Framework** built using **FastAPI** that demonstrates how multiple intelligent agents can be orchestrated using a clean, extensible architecture.

This project is designed to **teach and demonstrate agent-based system design**, not just API development.

---

## 📌 Why This Project Exists

Most AI projects:
- Hard-code logic
- Mix routing, execution, and reasoning
- Are difficult to extend

This project solves that by:
- Separating **reasoning**, **execution**, and **memory**
- Implementing a **true orchestrator**
- Supporting **multiple agent tasks using the same core framework**

---

## 🎯 Implemented Agent Tasks

This framework supports **three complete agent workflows**:

1. 📄 **PDF Analyzer Agent**
2. 📑 **Resume Analyzer Agent**
3. ❓ **Question & Answer (Q&A) Agent**

All tasks are handled by the **same agent brain (Orchestrator)**.

---

## 🧠 What Is an Agent Here?

In this framework, an **agent** is:

> A system that receives an intent, reasons about the steps needed, executes actions via workers, stores context in memory, and returns a result.

Each agent task follows this lifecycle:

