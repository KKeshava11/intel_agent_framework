from core.task import Task

def qa_flow(agent, text: str, question: str):
    """
    Performs Q&A on the given text using the agent.
    Returns an answer to the question.
    """
    print(f"Running Q&A for question: {question}")

    def task_function():
        # Simple heuristic: look for sentences containing keywords
        sentences = text.split(".")
        question_keywords = question.lower().split()
        relevant = []
        for sent in sentences:
            if any(word in sent.lower() for word in question_keywords):
                relevant.append(sent.strip())

        if not relevant:
            return "No relevant information found in the document."

        # Combine relevant sentences as the "answer"
        answer = ". ".join(relevant)
        return answer

    task = Task(
        description=f"Q&A Task: {question}",
        func=task_function
    )

    result = agent.run_task(task)
    return result
