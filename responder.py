from managers.round_manager import RoundManager
from managers.participant_manager import ParticipantManager
from managers.task_manager import TaskManager
from handlers.show_round_handler import ShowRoundHandler
from handlers.show_rounds_handler import ShowRoundsHandler
from handlers.add_round_handler import AddRoundHandler
from handlers.show_participants_handler import ShowParticipantsHandler
from handlers.add_participant_handler import AddParticipantHandler
from handlers.roll_handler import RollHandler
from handlers.help_handler import HelpHandler

class Responder:
    def __init__(self, participant_manager: ParticipantManager, round_manager: RoundManager,
                 task_manager: TaskManager):
        self.participant_manager = participant_manager
        self.round_manager = round_manager
        self.task_manager = task_manager
        self.message_handlers = [ShowRoundsHandler(round_manager),
                                 AddRoundHandler(participant_manager, round_manager),
                                 ShowRoundHandler(participant_manager, round_manager, task_manager),
                                 ShowParticipantsHandler(participant_manager, round_manager),
                                 AddParticipantHandler(participant_manager, round_manager),
                                 RollHandler(participant_manager, round_manager, task_manager)]

        hh = HelpHandler(self.message_handlers)
        self.message_handlers.append(hh)

    def handle_message(self, message) -> str:
        message = message.lower()

        for handler in self.message_handlers:
            resp = handler(message)
            if resp:
                return resp
