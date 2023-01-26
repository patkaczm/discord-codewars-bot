from round import Round
from datetime import datetime, timedelta
import pytest


class TestRound:
    monday = datetime.strptime("23.01.2023 12:13:14", "%d.%m.%Y %H:%M:%S")

    def test_can_create_round_only_if_start_date_is_monday(self):
        Round(start_date=self.monday)
        with pytest.raises(Exception):
            for day_in_week in range(1, 7):
                Round(self.monday + timedelta(days=day_in_week))

    def test_round_cares_only_about_start_date__time_is_fixed_to_midnight(self):
        r = Round(start_date=self.monday)
        dates = r.get_dates()
        expected_start_date = datetime.strptime("23.01.2023 00:00:00", "%d.%m.%Y %H:%M:%S")
        assert dates.start_date == expected_start_date

    def test_round_has_fixed_end_time_for_a_second_before_midnight_on_sunday(self):
        r = Round(start_date=self.monday)
        dates = r.get_dates()
        expected_end_date = datetime.strptime("29.01.2023 23:59:59", "%d.%m.%Y %H:%M:%S")
        assert dates.end_date == expected_end_date

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
