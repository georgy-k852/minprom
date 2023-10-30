from abc import ABC

from db.storages import BaseAppContext


class BaseService(ABC):
    _context: BaseAppContext

    @property
    def context(self):
        if not self._context:
            raise NotImplemented
        return self._context
