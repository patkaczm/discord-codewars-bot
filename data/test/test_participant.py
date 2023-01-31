from data.participant import Participant


class TestParticipant:
    round_id = 13
    username = 'some_user'

    def test_participant_created_without_id_has_id_fixed(self):
        p = Participant(username=self.username, round_id=self.round_id)
        assert p.username == self.username
        assert p.round_id == self.round_id
        assert -1 == p.id

    def test_participant_created_with_id_has_id(self):
        id = 1234
        p = Participant(username=self.username, round_id=self.round_id, id=id)
        assert p.id == id
