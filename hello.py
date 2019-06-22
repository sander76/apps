import appdaemon.plugins.hass.hassapi as hass
import globals


class HelloWorld(hass.Hass):
    def initialize(self):
        self.log("Hello from AppDaemon")
        self.log("You are now ready to run Apps!")


class AwayMode(hass.Hass):
    def initialize(self):
        self.log("init away mode.")

        self.listen_state(self.on_away_state, "input_boolean.away")

    def on_away_state(self, entity, attribute, old, new, kwargs):
        self.log(new)
        if new == "on":
            globals.away_mode = True
            self.log("Away is on")
        else:
            globals.away_mode = False
            self.log("Away is off")
        self.notify("Away mode: {}".format(new),name="sander")

