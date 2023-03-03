import utils
import socket

from vendor.domain import Domain


class System(Domain):
    @property
    def hostname(self):
        return socket.gethostname()

    def dump(self):
        return utils.dump(self)
