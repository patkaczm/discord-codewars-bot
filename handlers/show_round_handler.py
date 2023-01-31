import re
from managers.round_manager import RoundManager
from managers.participant_manager import ParticipantManager


class ShowRoundHandler:
    def __init__(self, participant_manager: ParticipantManager, round_manager: RoundManager):
        self.participant_manager = participant_manager
        self.round_manager = round_manager

    def __call__(self, message):
        print(f"Check: {self.__class__.__name__}")
        regex = r'\/show round (\d+)'
        matches = re.finditer(regex, message, re.MULTILINE)
        ret = ''
        for match in matches:
            round_id = match.group(1)
            ret += self.__handle_show_round__(round_id)
        return ret if ret != '' else None

    def __handle_show_round__(self, round_id):
        round = self.round_manager.get_round(round_id=round_id)
        participants = self.participant_manager.get_participants_for_round(round=round)
        return str(round) + '\n' + str(participants)