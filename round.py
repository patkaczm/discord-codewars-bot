from datetime import datetime
from dataclasses import dataclass, field


@dataclass(frozen=True, kw_only=True)
class Round:
    start_date: datetime
    end_date: datetime
    id: int = field(default=-1, repr=False)

    def __post_init__(self):
        if self.start_date > self.end_date:
            raise Exception('Start date must be before end date')