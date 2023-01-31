from ext.database import Database
from data.task import Task
from data.cw_task import CwTask
from managers.round_manager import RoundManager


class TaskManager:
    def __init__(self, database: Database, round_manager: RoundManager):
        self.database = database
        self.round_manager = round_manager
        self.tasks = []
        self.cw_tasks = []
        self.fetch()

    def fetch(self):
        for task in self.database.get_cw_tasks():
            self.cw_tasks.append(CwTask(id=task[0], kyu=task[1], cw_id=task[2], name=task[3]))

        for task in self.database.get_tasks():
            cw_task = self.get_cw_task(task[2])
            print(f'{task}\nLooking for task {task[2]} found {cw_task}')
            round = self.round_manager.get_round(task[1])
            self.tasks.append(Task(round=round, cw_task=cw_task))

    def get_cw_tasks(self, kyu):
        ret = []
        for task in self.cw_tasks:
            if task.kyu == kyu:
                ret.append(task)
        return ret

    def get_cw_task(self, id):
        for task in self.cw_tasks:
            if task.id == id:
                return task

    def add_task_to_round(self, cw_task, round):
        self.tasks.append(Task(round=round, cw_task=cw_task))
        self.database.add_task(round.id, cw_task.id)

    def get_tasks(self, round):
        ret = []
        for task in self.tasks:
            if task.round == round:
                ret.append(task)
        return ret
