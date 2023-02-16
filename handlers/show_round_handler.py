import re
from managers.round_manager import RoundManager
from managers.participant_manager import ParticipantManager
from managers.task_manager import TaskManager
from ext.codewars import CodewarsAPI, CodewarsTasks, CodewarsDoneTasksFormatter


class ShowRoundHandler:
    def __init__(self, participant_manager: ParticipantManager, round_manager: RoundManager, task_manager: TaskManager):
        self.participant_manager = participant_manager
        self.round_manager = round_manager
        self.task_manager = task_manager

    def help(self):
        return '/show {round_id} - shows details of round with given id'

    def __call__(self, message):
        print(f"Check: {self.__class__.__name__}")
        regex = r'\/show round (-?\d+)'
        matches = re.finditer(regex, message, re.MULTILINE)
        ret = ''
        for match in matches:
            round_id = match.group(1)
            ret += self.__handle_show_round__(round_id)
        return '```\n' + ret + '\n```' if ret != '' else None

    def __handle_show_round__(self, round_id):
        try:
            round = self.round_manager.get_round(round_id=round_id)
            participants = self.participant_manager.get_participants_for_round(round=round)
            tasks = self.task_manager.get_tasks(round)
            c = CodewarsAPI()

            p_s = []
            for participant in participants:
                dt = CodewarsDoneTasksFormatter().format(
                    CodewarsTasks(c.get_user_done_tasks(participant.username)).filter(language='python'), id=True)
                not_done = [t.cw_task.name for t in tasks if t.cw_task.cw_id not in dt]
                p_s.append(f'{participant} (To do: {not_done})')

            return str(round) + '\n' \
                   + "Participants:\n" + '\n'.join(p_s) + '\n' \
                   + "Tasks: \n" + '\n'.join([str(t) for t in tasks])
        except Exception as e:
            return str(e)
