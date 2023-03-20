"""
======================================================== test session starts ========================================================
platform darwin -- Python 3.11.1, pytest-7.2.0, pluggy-1.0.0
rootdir: /Users/savarin/Development/python/gpt-raft
plugins: anyio-3.6.2
collected 1 item

src/test_raftlog.py F                                                                                                         [100%]

============================================================= FAILURES ==============================================================
_____________________________________________________ test_append_entries_paper _____________________________________________________

logs_by_identifier = {'a': [LogEntry(term=1, item='1'), LogEntry(term=1, item='1'), LogEntry(term=1, item='1'), LogEntry(term=4, item='4'),...Entry(term=1, item='1'), LogEntry(term=4, item='4'), LogEntry(term=4, item='4'), LogEntry(term=5, item='5'), ...], ...}

    def test_append_entries_paper(logs_by_identifier):
        # Figure 7a
>       assert not raftlog.append_entries(
            logs_by_identifier["a"], 9, 6, [raftlog.LogEntry(6, "6")]
        )
E       AssertionError: assert not True
E        +  where True = <function append_entries at 0x1100b04a0>([LogEntry(term=1, item='1'), LogEntry(term=1, item='1'), LogEntry(term=1, item='1'), LogEntry(term=4, item='4'), LogEntry(term=4, item='4'), LogEntry(term=5, item='5'), ...], 9, 6, [LogEntry(term=6, item='6')])
E        +    where <function append_entries at 0x1100b04a0> = raftlog.append_entries

src/test_raftlog.py:70: AssertionError
====================================================== short test summary info ======================================================
FAILED src/test_raftlog.py::test_append_entries_paper - AssertionError: assert not True
========================================================= 1 failed in 0.07s =========================================================
"""
from dataclasses import dataclass
from typing import List, Union

@dataclass
class LogEntry:
    term: int
    item: str

def append_entries(
    log: List[LogEntry],
    leader_term: int,
    prev_log_index: int,
    entries: List[LogEntry],
) -> bool:
    """
    Append entries to the log following the Raft consensus algorithm.

    Args:
        log: The log to append entries to.
        leader_term: The term of the leader.
        prev_log_index: The index of the last log entry before the new entries.
        entries: The list of entries to append.

    Returns:
        True if the entries were appended, False otherwise.
    """

    if prev_log_index >= len(log) or log[prev_log_index].term >= leader_term:
        return False

    # Remove any conflicting entries and append new entries
    log[:] = log[: prev_log_index + 1] + entries
    return True
