import sys

from .middleware import Middleware
from .server import Server
if sys.version_info >= (3, 5):  # pragma: no cover
    from .asyncio_server import AsyncServer
else:
    AsyncServer = None

__version__ = '1.1.2'

__all__ = [__version__, Middleware, Server]
if AsyncServer is not None:  # pragma: no cover
    __all__.append(AsyncServer)
