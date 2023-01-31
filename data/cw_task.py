from dataclasses import dataclass, field


@dataclass(frozen=True, kw_only=True)
class CwTask:
    kyu: int
    cw_id: str
    name: str
    id: int = field(default=-1, repr=False)
