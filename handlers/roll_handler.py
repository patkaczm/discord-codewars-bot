import re
from managers.round_manager import RoundManager
from managers.participant_manager import ParticipantManager
from managers.task_manager import TaskManager
from random import choices


class RollHandler:
    def __init__(self, participant_manager: ParticipantManager, round_manager: RoundManager, task_manager: TaskManager):
        self.participant_manager = participant_manager
        self.round_manager = round_manager
        self.task_manager = task_manager

    def help(self):
        return '/roll {round_id} {number of tasks} - adds random {number of tasks} to round with given id'

    def __call__(self, message):
        print(f"Check: {self.__class__.__name__}")
        regex = r'\/roll (\d+) (\d+)'
        matches = re.finditer(regex, message, re.MULTILINE)
        ret = ''
        for match in matches:
            round_id = int(match.group(1))
            no_tasks = int(match.group(2))
            ret += self.__handle_roll_tasks__(round_id, no_tasks)
        return ret if ret != '' else None

    def __handle_roll_tasks__(self, round_id: int, no_tasks: int):
        tasks = self.task_manager.get_cw_tasks(6)
        print(tasks)
        round = self.round_manager.get_round(round_id)
        print(round)
        random_tasks = choices(tasks, k=no_tasks)
        print(random_tasks)
        for task in random_tasks:
            self.task_manager.add_task_to_round(task, round)

        return str(random_tasks) if random_tasks else f'There are no {no_tasks} tasks for kyu: {6} available'
