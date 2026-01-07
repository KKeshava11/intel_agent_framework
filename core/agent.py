from core.memory import Memory
from core.executor import Executor

class Agent:
    def __init__(self, name: str):
        self.name = name
        self.memory = Memory()
        self.executor = Executor()

    def run_task(self, task):
        print(f"[Agent: {self.name}] Running task: {task.description}")
        result = self.executor.execute(task)
        self.memory.store(task.description, result)
        return result
