from abc import ABC, abstractmethod

class SensorReading(ABC):
    def __init__(self, sensor_id, location, temperature, operator_id):
        self.sensor_id = sensor_id
        self.location = location
        self.temperature = temperature
        self.operator_id = operator_id
    @abstractmethod
    def handle(self): pass

class NormalSensor(SensorReading):
    def handle(self):
        return f"{self.sensor_id} di {self.location} ({self.temperature}°C) -> NORMAL"

class WarningSensor(SensorReading):
    def handle(self):
        op = self.operator_id if self.operator_id else "NULL - Cek!"
        return f"{self.sensor_id} di {self.location} ({self.temperature}°C) -> WARNING ke op {op}"

class DangerSensor(SensorReading):
    def handle(self):
        op = self.operator_id if self.operator_id else "AUTO-SHUTDOWN"
        return f"{self.sensor_id} di {self.location} ({self.temperature}°C) -> DANGER!!! Op {op}"

def sensor_factory(data):
    if data['status'] == "DANGER":
        return DangerSensor(data['sensor_id'], data['location'], data['temperature'], data['operator_id'])
    elif data['status'] == "WARNING":
        return WarningSensor(data['sensor_id'], data['location'], data['temperature'], data['operator_id'])
    else:
        return NormalSensor(data['sensor_id'], data['location'], data['temperature'], data['operator_id'])