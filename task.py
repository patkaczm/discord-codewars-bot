from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class Task:
    round_id: int
    cw_task_id: int
