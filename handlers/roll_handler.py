import re
from managers.round_manager import RoundManager
from managers.participant_manager import ParticipantManager


class RollHandler:
    def __init__(self, participant_manager: ParticipantManager, round_manager: RoundManager):
        self.participant_manager = participant_manager
        self.round_manager = round_manager

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
        round = self.round_manager.get_round(round_id=round_id)
        participants = self.participant_manager.get_participants_for_round(round=round)

        return str(round) + '\n' + str(participants)
