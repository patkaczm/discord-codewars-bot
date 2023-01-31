from ext.codewars import CodewarsAPI
from data.participant import Participant
from ext.database import Database
from managers.round_manager import RoundManager


class ParticipantManager:
    def __init__(self, round_manager: RoundManager, database: Database):
        self.round_manager = round_manager
        self.database = database
        self.participants = []
        self.fetch()

    def fetch(self):
        for participant in self.database.get_participants():
            self.participants.append(Participant(id=participant[0], username=participant[1],
                                                 round=self.round_manager.get_round(participant[2])))

    def get_participants_for_round(self, round):
        ret = []
        for participant in self.participants:
            if participant.round.id == round.id:
                ret.append(participant)

        return ret

    def add_participant(self, username, round):
        if not CodewarsAPI().does_user_exist(username):
            raise Exception(f'User with name={username} does not exist')

        for p in self.participants:
            if p.username == username and p.round == round:
                raise Exception(f'User with name={username} has already been added to round with id={round.id}')

        # @todo mby Participant should hold an Round instead of round_id
        self.participants.append(Participant(username=username, round=round))
        self.database.add_participant(username, round.id)

    def remove_participant(self, username, round):
        # check if added
        # cannot remove participant if now() > start_date
        #
        raise (Exception("Not yet implemented"))
