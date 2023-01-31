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

    def __repr__(self):
        start = datetime.strftime(self.start_date, '%d.%m.%Y %H:%M:%S')
        end = datetime.strftime(self.end_date, '%d.%m.%Y %H:%M:%S')

        return f"Round {self.id} (start={start} end={end})"
