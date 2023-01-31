import discord
import os
from responder import Responder
from managers.participant_manager import ParticipantManager
from managers.round_manager import RoundManager
from ext.database import Database
from managers.task_manager import TaskManager


class Bot:
    def __init__(self):
        self.database = Database('test_database.sqlite')
        self.round_manager = RoundManager(database=self.database)
        self.participant_manager = ParticipantManager(database=self.database, round_manager=self.round_manager)
        self.task_manager = TaskManager(database=self.database)
        self.responder = Responder(participant_manager=self.participant_manager, round_manager=self.round_manager,
                                   task_manager=self.task_manager)

    async def send_message(self, message, user_message):
        try:
            response = self.responder.handle_message(user_message)
            await message.channel.send(response)
        except Exception as e:
            print(e)

    def run_discord_bot(self):
        client = discord.Client(intents=discord.Intents.all())

        @client.event
        async def on_ready():
            print(f'{client.user} is now running!')

        @client.event
        async def on_message(message):
            if message.author == client.user:
                return

            username = str(message.author)
            user_message = str(message.content)
            channel = str(message.channel)

            print(f'{username} said {user_message} on {channel}')

            await self.send_message(message, user_message)

        client.run(os.environ.get('TOKEN'))
