import re
from managers.round_manager import RoundManager
from managers.participant_manager import ParticipantManager


class AddParticipantHandler:
    def __init__(self, participant_manager: ParticipantManager, round_manager: RoundManager):
        self.participant_manager = participant_manager
        self.round_manager = round_manager

    def __call__(self, message):
        print(f"Check: {self.__class__.__name__}")
        regex = r"\/add participant (\w+) (\d+)"
        matches = re.finditer(regex, message, re.MULTILINE)
        ret = ''
        for match in matches:
            username = match.group(1)
            round_id = match.group(2)
            print(f'Match {match.group()}\nUsername: {username}\nRoundId: {round_id}')
            ret += self.__handle_add_round__(username, round_id)
        return ret if ret != '' else None

    def __handle_add_round__(self, username: str, round_id: int):
        round = self.round_manager.get_round(round_id)
        self.participant_manager.add_participant(username, round)

        return f'Participant {username} has been added to round {round.id}'
