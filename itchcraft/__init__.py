"""
Usage example:

.. code:: python

   from itchcraft.api import Api

   api = Api()
   api.hello()
"""

# Re-export these symbols
# (This promotes them from itchcraft.api to itchcraft)
from itchcraft.api import Api as Api

from itchcraft.version import version

__all__ = [
    # Modules that every subpackage should see
    'settings',
]

__version__ = version()
