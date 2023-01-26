class Participant:
    def __init__(self, id, username, round_id):
        self.id = id
        self.username = username
        self.round_id = round_id

    def get_id(self):
        return self.id

    def get_username(self):
        return self.username

    def get_round_id(self):
        return self.round_id


