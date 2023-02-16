from bot import Bot
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

if __name__ == '__main__':
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-d", "--database", default="test_database.sqlite", help="Database name")
    args = vars(parser.parse_args())

    bot = Bot(args['database'])
    bot.run_discord_bot()
