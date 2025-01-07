"""Nexia Thermostat Sensor."""

from typing import NamedTuple


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
# end class NexiaSensor
