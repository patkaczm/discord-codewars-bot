import discord
import bot_responses


async def send_message(message, user_message):
    try:
        response = bot_responses.handle_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTA2MzM3NjAwNDk1OTE5NTE4Ng.Gm8_JA.scIuXpbqYjpBjGULyDcLUF8ciuHCmLbZIJmFJg'
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

        await send_message(message, user_message)

    client.run(TOKEN)