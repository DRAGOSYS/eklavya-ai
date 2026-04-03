# 🎯 Eklavya: AI-Powered Multi-Agent Learning Assistant

**Eklavya** is an intelligent pedagogical pipeline designed to automate the generation, validation, and refinement of educational content. Built with a **Multi-Agent Orchestration** architecture, it ensures that learning materials are not only accurate but also grade-appropriate and structurally sound.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](YOUR_DEPLOYED_APP_URL_HERE)

---

## 🚀 The Multi-Agent Workflow
Unlike standard single-prompt AI tools, Eklavya utilizes a sequential pipeline of specialized agents to minimize "hallucinations" and maximize pedagogical quality.



1.  **Generator Agent:** Crafts comprehensive lesson explanations and relevant MCQs based on the user's topic and target grade.
2.  **Reviewer Agent:** Acts as an automated quality gate, evaluating the content for clarity, accuracy, and grade-level suitability.
3.  **Refinement Agent:** Triggered only if the Reviewer flags an issue, this agent re-processes the content using the specific feedback provided to ensure a perfect final output.

---

## ✨ Key Features
- **Sequential Self-Correction:** Automated "Pass/Fail" logic between agents ensures high-fidelity results.
- **Dynamic Grade Scaling:** Content adjusts complexity automatically for Grades 1 through 12.
- **Interactive UI:** Built with Streamlit, providing real-time status updates on agent "thoughts" and final lesson delivery.
- **JSON-Schema Driven:** High reliability through structured data exchange between AI models.

---

## 🛠️ Tech Stack
- **Core LLM:** Gemini 3 Flash (via `google-genai` SDK)
- **Framework:** Streamlit (Python)
- **Deployment:** Streamlit Community Cloud / GitHub CI/CD

---

## 📦 Local Installation

1. **Clone the repository:**
   ```bash
   git init
   git remote add origin (https://github.com/DRAGOSYS/eklavya-ai.git)
   git pull origin main
