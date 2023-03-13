import os
import sys
import utils
import socket
import shutil
import psutil

from core.domain import Domain
from utils import to_GB, to_MB, MAX_INT32BIT


class System(Domain):
    def __init__(self, runner):
        self.runner = runner

    @property
    def architecture(self):
        return '64bit' if sys.maxsize > MAX_INT32BIT else '32bit'
    
    @property
    def cpu_usage(self):
        cpu_load_last_minute = psutil.getloadavg()[0]
        return round((cpu_load_last_minute / os.cpu_count()) * 100, 1)

    @property
    def hostname(self):
        return socket.gethostname()
    
    @property
    def ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('192.255.255.255', 1))
            ip = s.getsockname()[0]
        except:
            ip = '127.0.0.1'
        finally:
            s.close()

        return ip
    
    @property
    def disk_space(self):
        total, used, _ = shutil.disk_usage("/")
        return {
            'total': to_GB(total),
            'used': to_GB(used),
        }
    
    @property
    def ram_space(self):
        total, _, _, used, _ = psutil.virtual_memory()[:5]
        return {
            'total': to_MB(total),
            'used': to_MB(used),
        }

    def dump(self):
        return utils.dump(self)
