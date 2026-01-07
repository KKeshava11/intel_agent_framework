from core.task import Task

def run_pdf_flow(agent, pdf_text: str):
    """
    Processes PDF text using the Agent framework.
    Returns total lines, total words, and a preview.
    """
    print("Processing PDF content...")

    def task_function():
        lines = pdf_text.splitlines()
        words = pdf_text.split()
        result = {
            "total_lines": len(lines),
            "total_words": len(words),
            "preview": pdf_text[:500]  # first 500 characters
        }
        return result

    task = Task(
        description="PDF Extraction Task",
        func=task_function
    )

    result = agent.run_task(task)
    return result
