# RAG Chatbot with LangChain, IBM Watsonx, and Gradio
This project is a **Retrieval-Augmented Generation (RAG) Chatbot** that allows users to upload a document (PDF or text) and ask natural language quesitons. It uses **IBM Watsonx foundation models**, **LangChain**, and **Gradio** to build an interactive and intelligent document-based Q&A system.

---
## Features

- Upload a PDF or `.txt` document
- Ask quesitons about the uploaded file
- Uses LangChain for chunking and retrieval
- Embedding powered by IBM Watsonx
- Large Language Model (LLM) integration for response generation
- Gradio frontend for a user-friendly experience

---

## Getting started

### 1. Clone the repo 

```bash
git clone https:// github.com](https://github.com/JulietaCCollado/RAG-QABot-.git
```
### 2. Create and activate a virtual environment

```bash
python -m venv venv
# for PowerShell (use the excecution policy fix if needed):
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash 
python main.py
```
Then go to http://localhost:7860 in your browser.

## Example Queries

- `What is this paper talking about?`<br>
- `Which policies are mentioned in this file?`<br>
- `What is the smoking policy?`

## Technologies Used

- LangChain
- IBM Watsonx
- Gradio
- Python 3.11+

## Author
`Julieta Collado - AI Engineering Student`

#### This project is for educational purposes only ###
