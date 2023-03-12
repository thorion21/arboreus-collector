import inspect


DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

MAX_INT32BIT = 2 ** 32 - 1

B2GB = 1 / (10 ** 9)
B2GiB = 1 / (2 ** 30)
B2MB = 1 / (10 ** 6)
B2MiB = 1 / (2 ** 20)


to_GB = lambda x: round(x * B2GB, 2)
to_GiB = lambda x: round(x * B2GiB, 2)
to_MB = lambda x: round(x * B2MB, 1)
to_MiB = lambda x: round(x * B2MiB, 1)


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
