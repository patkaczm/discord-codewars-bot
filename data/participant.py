from dataclasses import dataclass, field
from data.round import Round


@dataclass(frozen=True, kw_only=True)
class Participant:
    username: str
    round: Round
    id: int = field(default=-1, repr=False)

    def __repr__(self):
        return self.username
