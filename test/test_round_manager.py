from managers.round_manager import RoundManager
from unittest.mock import MagicMock
from pytest import raises
from data.round import Round
from datetime import datetime


class TestRoundManager:
    rounds = [(1, '28.01.2023 16:00:00', '28.01.2023 17:00:00')]
    new_round = ('29.01.2023 16:00:00', '29.01.2023 17:00:00')

    def test_round_manager_calls_database_to_get_data_on_fetch(self):
        mm = MagicMock()
        r = RoundManager(mm)

        mm.get_rounds.return_value = self.rounds
        r.fetch()

        mm.get_rounds.assert_called_once()

    def test_round_manager_raises_when_trying_to_get_round_which_does_not_exist(self):
        mm = MagicMock()
        r = RoundManager(mm)
        some_round_id = 14

        with raises(Exception):
            r.get_round(some_round_id)

    def test_round_manager_returns_round_if_round_is_stored_in_db(self):
        mm = MagicMock()
        r = RoundManager(mm)

        mm.get_rounds.return_value = self.rounds
        r.fetch()

        round = r.get_round(self.rounds[0][0])
        expected_start_date = datetime.strptime(self.rounds[0][1], '%d.%m.%Y %H:%M:%S')
        expected_end_date = datetime.strptime(self.rounds[0][2], '%d.%m.%Y %H:%M:%S')
        expected_round = Round(id=self.rounds[0][0], start_date=expected_start_date, end_date=expected_end_date)
        assert round == expected_round

    def test_get_rounds_returns_a_dict_with_rounds_stored_in_db_and_new_once(self):
        mm = MagicMock()
        r = RoundManager(mm)

        mm.get_rounds.return_value = self.rounds
        r.fetch()
        r.add_round(datetime.strptime(self.new_round[0], '%d.%m.%Y %H:%M:%S'),
                    datetime.strptime(self.new_round[1], '%d.%m.%Y %H:%M:%S'))

        expected = {
            'stored': [
                Round(id=self.rounds[0][0], start_date=datetime.strptime(self.rounds[0][1], '%d.%m.%Y %H:%M:%S'),
                      end_date=datetime.strptime(self.rounds[0][2], '%d.%m.%Y %H:%M:%S'))],
            'new': [Round(start_date=datetime.strptime(self.new_round[0], '%d.%m.%Y %H:%M:%S'),
                          end_date=datetime.strptime(self.new_round[1], '%d.%m.%Y %H:%M:%S'))]
        }

        assert r.get_rounds() == expected

    def test_commit_saves_data_in_database(self):
        mm = MagicMock()
        r = RoundManager(mm)
        r.add_round(datetime.strptime(self.new_round[0], '%d.%m.%Y %H:%M:%S'),
                    datetime.strptime(self.new_round[1], '%d.%m.%Y %H:%M:%S'))
        r.commit()
        mm.add_round.assert_called_once()
