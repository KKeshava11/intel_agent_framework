class Memory:
    def __init__(self):
        self.data = []

    def store(self, task, result):
        entry = {
            "task": task,
            "result": result
        }
        self.data.append(entry)

    def get_all(self):
        return self.data
