"""
.. include:: ../README.md

## API Documentation
"""

# Re-export these symbols
# (This promotes them from itchcraft.api to itchcraft)
from itchcraft.api import Api as Api

from itchcraft.version import version

__all__ = [
    # Tell pdoc to pick up all re-exported symbols
    'Api',

    # Modules that every subpackage should see
    # (This also exposes them to pdoc)
    'api',
    'settings',
]

__version__ = version()
