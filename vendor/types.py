from enum import Enum


class DomainType(Enum):
    System = "system"
    Sensors = "sensors"
    Medium = "medium"
    Unknown = "unknown"
    All = "all"
