class Task:
    def __init__(self, description, func):
        self.description = description
        self.func = func

    def run(self):
        return self.func()
