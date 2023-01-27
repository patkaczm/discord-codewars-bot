from round import Round
from datetime import datetime, timedelta
import pytest


class TestRound:
    start_date = datetime.strptime("23.11.2023 12:33:44", "%d.%m.%Y %H:%M:%S")
    end_date = start_date + timedelta(days=1)

    def test_round_created_without_id_has_id_fixed(self):
        r = Round(start_date=self.start_date, end_date=self.end_date)
        assert r.start_date == self.start_date
        assert r.end_date == self.end_date
        assert r.id == -1

    def test_round_created_with_id_has_id(self):
        id = 13
        r = Round(id=id, start_date=self.start_date, end_date=self.end_date)
        assert r.id == id

    def test_round_throws_if_start_date_is_before_end_date(self):
        with pytest.raises(Exception):
            Round(start_date=self.end_date, end_date=self.start_date)


# r = Round()
# r.add_participant(username)      -> userManager
# r.remove_participant(username)   -> userManager
# r.roll({5: 2, 6: 3})             -> fetches tasks done by users (A) and tasks from 'codewars' (B) and
#                                     performes set substr (B-A) and returns random tasks from (B-A)
# r.check_tasks_done_by_participant(username) -> checks tasks done by participant
# r.check_progress() -> checks tasks done by all participants
# r.get_status() -> returns status [not_started_yet | in_progress | done]
# r.get_dates() -> returns {'start_date': date, 'end_date': date}


# rm = RoundManager()
# rm.get_current_round() -> returns current_round or None
# rm.get_next_round() -> returns next_round or None
# rm.add_next_round(r) -> adds next round r or replaces next_round if available
