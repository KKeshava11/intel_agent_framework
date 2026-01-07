from core.task import Task

def sample_flow(agent):
    print("Running sample flow...")

    def task_function():
        return "Sample task completed"

    task = Task(
        description="Sample Task",
        func=task_function
    )

    result = agent.run_task(task)
    print("Result:", result)
