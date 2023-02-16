from managers.round_manager import RoundManager


class ShowRoundsHandler:
    def __init__(self, round_manager: RoundManager):
        self.round_manager = round_manager

    def help(self):
        return '/show rounds - return rounds\' list'

    def __call__(self, message):
        print(f"Check: {self.__class__.__name__}")
        if message == '/show rounds':
            return self.__handle_show_rounds__()
        return None

    def __handle_show_rounds__(self):
        msg = '```'
        for round in self.round_manager.get_rounds():
            msg += str(round) + '\n'
        msg += '```'
        return msg
