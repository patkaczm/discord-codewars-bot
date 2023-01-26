from participant import Participant


class TestParticipant:
    id = 1
    round_id = 13
    username = 'some_user'
    p = Participant(id, username, round_id)

    def test_participant_has_id(self):
        assert self.id == self.p.get_id()

    def test_participant_has_username(self):
        assert self.username == self.p.get_username()

    def test_participant_has_round_id(self):
        assert self.round_id == self.p.get_round_id()