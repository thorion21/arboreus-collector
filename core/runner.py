from threading import Thread

from .routine import Routine


class Runner:
    def __init__(self):
        self.routines = {}

    def register_routine(self, key, routine):
        if not isinstance(routine, Routine):
            raise TypeError("Provided item is not a routine")
        
        if key in self.routines:
            raise ValueError(f"Duplicate routine key `{key}`")

        routine_thr = Thread(target=routine.loop)
        self.routines[key] = {
            'routine': routine,
            'thread' : routine_thr,
        }
        routine_thr.start()

    def collect(self, key):
        if not key in self.routines:
            raise TypeError(f"There is no runner with key `{key}`")
        
        return self.routines[key]['routine'].collect()
