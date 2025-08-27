"""
eFleetScheduler - Electric Fleet Scheduling Tool
"""

# src/efleetscheduler/__init__.py

__version__ = "0.0.2"
__author__ = "Carolina Gil Ribeiro"

# Re-export public API from submodules
from .schedule_generator_1 import ScheduleGenerator  # adjust names to what you actually export
from .schedule_generator_2 import generate_schedules
from .schedule_configure import schedule_configure
from .generate_graphs import generate_graphs

__all__ = [
    "ScheduleGenerator",
    "generate_schedules",
    "schedule_configure",
    "generate_graphs",
]
