import gradio as gr
from src.retriever import retriever_qa


def main():
    rag_application = gr.Interface(
        fn=retriever_qa,
        allow_flagging='never',
        inputs=[
            gr.File(label="Upload PDF File", file_count="single", file_types=['.pdf'], type="filepath"),
            gr.Textbox(label="Input Query", lines=2, placeholder="Type your question here...")
        ],
        outputs=gr.TextBox(label='Output'),
        title="RAG Chatbox",
        description="Upload a PDF document asn ask any question. The chatbox will try to answer using the provided document."
    )
    rag_application.launch(server_name="0.0.0.0", server_port=7860)

if __name__ == "__main__":
    main()
