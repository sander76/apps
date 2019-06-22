import datetime

import appdaemon.plugins.hass.hassapi as hass

ATTRIBUTES = "attributes"


class BatteryWatcher(hass.Hass):
    """Check battery components every x time on a daily basis."""

    def initialize(self):
        time = datetime.time(20, 0, 0)
        self.run_daily(self.check_batteries, time)

    def check_batteries(self, **kwargs):
        """Check state of all battery components."""

        binary_sensors = self.get_state(entity="binary_sensor")

        for entity_id, sensor in binary_sensors.items():

            device_class = sensor[ATTRIBUTES]["device_class"]

            if not device_class == "battery":
                continue

            # self.log(device_class)

            state = sensor["state"]

            if not state == "on":
                continue

            friendly_name = sensor[ATTRIBUTES]["friendly_name"]

            # self.log(entity_id)
            # self.log(sensor[ATTRIBUTES]["friendly_name"])
            # self.log(sensor)

            self.notify(
                "Device\n{}\n\n has an empty battery".format(friendly_name),
                name="sander",
            )
