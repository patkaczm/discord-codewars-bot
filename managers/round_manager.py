from ext.database import Database
from datetime import datetime
from data.round import Round


class RoundManager:
    def __init__(self, database: Database):
        self.database = database
        self.rounds = []
        self.date_format = '%d.%m.%Y %H:%M:%S'
        self.fetch()

    def fetch(self):
        for round in self.database.get_rounds():
            start_date = datetime.strptime(round[1], self.date_format)
            end_date = datetime.strptime(round[2], self.date_format)
            self.rounds.append(Round(id=round[0], start_date=start_date, end_date=end_date))

    def get_round(self, round_id: int):
        for round in self.rounds:
            if round.id == int(round_id):
                return round

        raise Exception(f'Round with id={round_id} does not exist')

    def get_rounds(self):
        return self.rounds

    def add_round(self, start_date: datetime, end_date: datetime):
        start_date_str = datetime.strftime(start_date, self.date_format)
        end_date_str = datetime.strftime(end_date, self.date_format)
        id = self.database.add_round(start_date=start_date_str, end_date=end_date_str)
        self.rounds.append(Round(id=id, start_date=start_date, end_date=end_date))
        return id
