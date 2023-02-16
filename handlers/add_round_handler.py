import re
from managers.round_manager import RoundManager
from managers.participant_manager import ParticipantManager
from datetime import datetime


class AddRoundHandler:
    def __init__(self, participant_manager: ParticipantManager, round_manager: RoundManager):
        self.participant_manager = participant_manager
        self.round_manager = round_manager

    def help(self):
        return "/add round {start date} {end date} - adds round, date must follow format (%d.%m.%Y %H:%M:%S)"

    def __call__(self, message):
        print(f"Check: {self.__class__.__name__}")
        regex = r"\/add round (\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2}) (\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2})"
        matches = re.finditer(regex, message, re.MULTILINE)
        ret = ''
        for match in matches:
            start = match.group(1)
            end = match.group(2)
            print(f'Match {match.group()}\nStart: {start}\nEnd: {end}')
            ret += self.__handle_add_round__(start_date=start, end_date=end)
        return ret if ret != '' else None

    def __handle_add_round__(self, start_date: str, end_date: str):
        id = self.round_manager.add_round(start_date=datetime.strptime(start_date, '%d.%m.%Y %H:%M:%S'),
                                          end_date=datetime.strptime(end_date, '%d.%m.%Y %H:%M:%S'))

        return f'Round {start_date} {end_date} added with id: {id}'
