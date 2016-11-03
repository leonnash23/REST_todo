class Task:
    def __init__(self, task_id: int, title: str, des: str, done: bool):
        self.done = done
        self.des = des
        self.title = title
        self.task_id = task_id

    def get_dict(self):
        return {
            'id': self.task_id,
            'title': self.title,
            'description': self.des,
            'done': self.done
        }
