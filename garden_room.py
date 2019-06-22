import appdaemon.plugins.hass.hassapi as hass
import globals


class Wrc6(hass.Hass):
    def initialize(self):
        self.log("init wrc6")
        self._name = self.args["name"]
        self.listen_event(self.on_press, "homematic.keypress")

        # self.listen_state(self.on_away_state, "input_boolean.away")

    def on_press(self, event_name, data, kwargs):
        self.log(data)
        name = data.get("name")
        if not name == self._name:
            self.log("no match in name or address")
            return

        channel = data.get("channel")
        param = data.get("param").lower()

        method_str = "on_channel_{}_{}".format(channel, param)
        method = getattr(self, method_str)
        if method:
            method()

    def on_channel_1_press_short(self):
        self.log("channel 1 press short")

    def on_channel_1_press_long(self):
        self.log("channel 1 press long")

    def on_channel_2_press_short(self):
        self.log("channel 2 press short")

    def on_channel_2_press_long(self):
        self.log("channel 2 press long")

    def on_channel_3_press_short(self):
        self.log("channel 3 press short")

    def on_channel_3_press_long(self):
        self.log("channel 3 press long")

    def on_channel_4_press_short(self):
        self.log("channel 4 press short")

    def on_channel_4_press_long(self):
        self.log("channel 4 press long")

    def on_channel_5_press_short(self):
        self.log("channel 5 press short")

    def on_channel_5_press_long(self):
        self.log("channel 5 press long")

    def on_channel_6_press_short(self):
        self.log("channel 6 press short")

    def on_channel_6_press_long(self):
        self.log("channel 6 press long")


class Wrc6Garden(Wrc6):
    def on_channel_1_press_short(self):
        self.call_service(
            "hue/hue_activate_scene", group_name="dining", scene_name="normal"
        )

    def on_channel_1_press_long(self):
        self.call_service(
            "hue/hue_activate_scene", group_name="dining", scene_name="full on"
        )

    def on_channel_2_press_short(self):
        self.call_service("light/turn_off", entity_id="light.dining")

    def on_channel_3_press_short(self):
        self.turn_on("script.living_default_on")

    def on_channel_4_press_short(self):
        self.turn_off("light.livingroom")
