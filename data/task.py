from dataclasses import dataclass
from .round import Round
from .cw_task import CwTask


@dataclass(frozen=True, kw_only=True)
class Task:
    round: Round
    cw_task: CwTask

    def __repr__(self):
        return f'{self.cw_task.name}(https://www.codewars.com/kata/{self.cw_task.cw_id})'
