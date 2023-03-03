import inspect


DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def dump(cls):
    return {
        cls.__class__.__name__.lower(): {
            name: getattr(cls, name)
            for name, _ in inspect.getmembers(
                cls.__class__, lambda x: isinstance(x, property)
            )
        }
    }


def present_domains(dct):
    return ", ".join([member.value for member in list(dct.keys())])
