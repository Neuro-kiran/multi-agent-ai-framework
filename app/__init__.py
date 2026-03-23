"""Multi-Agent AI Framework - Core package."""

__version__ = "0.1.0"
__author__ = "Kiran Marne"
__license__ = "MIT"

from . import config
from . import orchestrator
from . import memory
from . import tools
from . import agents

__all__ = [
    "config",
    "orchestrator",
    "memory",
    "tools",
    "agents",
]
