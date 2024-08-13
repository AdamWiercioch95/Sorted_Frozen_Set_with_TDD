from unittest.mock import Mock

from doubles_kata.alarm import Alarm
from doubles_kata.sensor import Sensor


# dummy
def test_alarm_is_off_by_default():
    dummy_sensor = 'sensor'
    alarm = Alarm(dummy_sensor)
    assert not alarm.is_alarm_on


# stub1
class StubSensor:
    def sample_pressure(self):
        return 15


def test_lower_pressure_activates_alarm():
    alarm = Alarm(sensor=StubSensor())
    alarm.check()
    assert alarm.is_alarm_on


# stub2
def test_normal_pressure_alarm_stays_off():
    stub_sensor = Mock(Sensor)
    stub_sensor.sample_pressure.return_value = 18
    alarm = Alarm(stub_sensor)
    alarm.check()
    assert not alarm.is_alarm_on
