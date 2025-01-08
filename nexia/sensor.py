"""Nexia Thermostat Sensor."""

from typing import NamedTuple, Optional


class NexiaSensor(NamedTuple):
    """Data object representing details of a nexia sensor"""
    id: int
    name: str
    type: str
    serial_number: str
    weight: float
    temperature: int
    temperature_valid: bool
    humidity: int
    humidity_valid: bool
    has_battery: bool
    battery_level: Optional[int]
    battery_valid: Optional[bool]

# end class NexiaSensor
