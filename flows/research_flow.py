from core.task import Task
from flows.summarize_flow import summarize_flow  # reuse existing summarization flow

def pdf_flow(agent, pdf_text: str):
    """
    Processes PDF text using the Agent framework.
    Returns a summary of the PDF content.
    """
    print("Processing PDF content for summary...")

    def task_function():
        # Ensure pdf_text is not None
        text = pdf_text or ""
        # Use existing summarize_flow to summarize the text
        result_summary = summarize_flow(agent, text)
        return result_summary

    task = Task(
        description="PDF Summary Task",
        func=task_function
    )

    try:
        result = agent.run_task(task)
    except Exception as e:
        result = {"error": str(e)}

    return result
