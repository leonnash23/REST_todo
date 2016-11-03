from model.Task import Task


class TaskList:
    def __init__(self):
        self.task_list = []

    def addTask(self, task: Task):
        self.task_list.append(task)

    def getTasks(self):
        ans = []
        for t in self.task_list:
            ans.append(t.get_dict())
        return ans
