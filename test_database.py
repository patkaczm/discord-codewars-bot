from database import Database
from unittest.mock import patch, MagicMock
from round import Round
from datetime import datetime
from participant import Participant

def dupa_print():
    print("Hello")


class TestDatabase:
    filename = 'test_database.sqlite'
    tables = [('ROUNDS',), ('TASKS',), ('CW_TASKS',), ('PARTICIPANTS',)]
    get_tables_query = "SELECT name from sqlite_master WHERE type='table'"

    def test_database_creates(self):
        Database(self.filename)

    @patch('database.sqlite3.connect')
    def test_database_creates_rounds_table_if_this_does_not_exist(self, connection_mock):
        connection_instance = MagicMock()
        connection_instance.cursor().execute = return_value = connection_instance
        connection_instance.cursor().execute().fetchall.return_value = self.tables

        connection_mock.return_value = connection_instance

        Database(self.filename)
        connection_mock.assert_called_once_with(self.filename)
        connection_instance.cursor().execute.assert_called_with(self.get_tables_query)


    def test_add_round_adds_round(self):
        database = Database(self.filename)
        round_start_date = datetime.strptime("23.01.2023", "%d.%m.%Y")
        round_end_date = datetime.strptime("29.01.2023", "%d.%m.%Y")
        database.add_round(round_start_date, round_end_date)

        actual_rounds = database.get_rounds()
        print(actual_rounds)
        assert actual_rounds[0] == (1, '23.01.2023', '29.01.2023')

    def test_add_participant_to_the_round(self):
        database = Database(self.filename)
        participant = Participant(-1, 'user', 1)
        database.add_participant(participant)

        print(database.get_participants(1))

    def test_add_cw_task(self):
        database = Database(self.filename)
        kyu, cw_id, name = (6, '58b1ae711fcffa34090000ea', 'Killer Garage Door')
        database.add_cw_task(kyu, cw_id, name)

        tasks = database.get_cw_tasks()
        print(tasks)