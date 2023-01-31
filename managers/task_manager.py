from ext.database import Database
from data.task import Task
from data.cw_task import CwTask


class TaskManager:
    def __init__(self, database: Database):
        self.database = database
        self.tasks = []
        self.cw_tasks = []
        self.fetch()

    def fetch(self):
        for task in self.database.get_tasks():
            self.tasks.append(Task(round_id=task[1], cw_task_id=task[2]))

        for task in self.database.get_cw_tasks():
            self.cw_tasks.append(CwTask(id=task[0], kyu=task[1], cw_id=task[2], name=task[3]))

    def get_cw_tasks(self, kyu):
        ret = []
        for task in self.cw_tasks:
            if task.kyu == kyu:
                ret.append(task)
        return ret

    def get_cw_task(self, cw_id):
        for task in self.cw_tasks:
            if task.cw_id == cw_id:
                return task

    def add_task_to_round(self, task, round):
        cw_task = self.get_cw_task(task.cw_id)
        self.tasks.append(Task(round_id=round.id, cw_task_id=cw_task.id))
        self.database.add_task(round.id, cw_task.id)

    def get_tasks(self, round):
        ret = []
        for task in self.tasks:
            if task.round_id == round.id:
                ret.append(task)
        return ret