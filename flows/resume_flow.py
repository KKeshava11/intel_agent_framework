from core.task import Task

def resume_flow(agent, resume_text: str):
    print("Analyzing resume...")

    def task_function():
        analysis = {}

        lines = resume_text.splitlines()
        analysis["total_lines"] = len(lines)

        keywords = ["python", "java", "sql", "machine learning", "data"]
        found = [k for k in keywords if k.lower() in resume_text.lower()]
        analysis["matched_keywords"] = found

        analysis["summary"] = (
            f"Resume has {len(lines)} lines. "
            f"Matched skills: {', '.join(found) if found else 'None'}"
        )

        return analysis

    task = Task(
        description="Resume Analysis Task",
        func=task_function
    )

    result = agent.run_task(task)
    return result
