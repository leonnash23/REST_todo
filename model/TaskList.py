from model.Task import Task


class TaskList:
    def __init__(self):
        self.task_list = []
        self.count = 0

    def addTask(self, task: Task):
        self.task_list.append(task)
        self.count += 1

    def getTasks(self):
        ans = []
        for t in self.task_list:
            ans.append(t.get_dict())
        return ans


