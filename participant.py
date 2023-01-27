from dataclasses import dataclass, field


@dataclass(frozen=True, kw_only=True)
class Participant:
    username: str
    round_id: int
    id: int = field(default=-1, repr=False)
