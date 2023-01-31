import re
from managers.round_manager import RoundManager
from managers.participant_manager import ParticipantManager


class ShowParticipantsHandler:
    def __init__(self, participant_manager: ParticipantManager, round_manager: RoundManager):
        self.participant_manager = participant_manager
        self.round_manager = round_manager

    def __call__(self, message):
        regex = r"\/show participants (\d+)"
        matches = re.finditer(regex, message, re.MULTILINE)
        ret = ''
        for match in matches:
            round_id = match.group(1)
            print(f'Match {match.group()}\nround_id: {round_id}')
            ret += self.__handle_show_participants__(round_id)
        return ret if ret != '' else None

    def __handle_show_participants__(self, round_id: id):
        round = self.round_manager.get_round(round_id)
        participants = self.participant_manager.get_participants_for_round(round)

        return ' '.join(participants) if participants else f'There are no participants for round {round_id}'
