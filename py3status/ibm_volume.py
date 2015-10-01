# -*- coding: utf8 -*-

from time import time
import subprocess

class Py3status:
    """
    """
    # available configuration parameters
    cache_timeout = 1

    def volume(self, i3s_output, i3s_config):
        with open("/proc/acpi/ibm/volume", "r") as f:
            level, mute = f.readlines()
            level = float(level.split(":")[1].strip()) / 14
            if "on" in mute or level == 0:
               text = "♪x"
            elif level == 1:
               text = "♪!"
            else:
               text = "♪%d" % (level*10)

        return {
            'cached_until': time() + self.cache_timeout,
            'color': '#2aa198',
            'full_text': text
        }

    def on_click(self, i3s_output, i3s_config, event_json):
        ret = subprocess.call("pavucontrol")


if __name__ == "__main__":
    from time import sleep
    x = Py3status()
    while True:
        print(x.volume([], []))
        sleep(1)
