# -*- coding: utf8 -*-

import subprocess
from time import time


class Py3status:
    """
    """
    # available configuration parameters
    cache_timeout = 1
    format = '{output}'

    values = {
        "us": ("#859900", "eng"),
        "rs": ("#2aa198", "ћир"),
        "rslatin": ("#2aa198", "lat")
    }

    def xkblayout(self, i3s_output, i3s_config):
        cmd = ["/usr/local/bin/xkblayout-state", "print", "%s%v"]
        ret = subprocess.check_output(cmd)

        color = "#dc322f"
        if ret in self.values:
            color, ret = self.values[ret]

        return {
            'cached_until': time() + self.cache_timeout,
            'color': color,
            'full_text': self.format.format(output=ret.rstrip())
        }

    def on_click(self, i3s_output, i3s_config, event_json):
        cmd = ["/usr/local/bin/xkblayout-state", "set", "+1"]
        ret = subprocess.check_output(cmd)


if __name__ == "__main__":
    from time import sleep
    x = Py3status()
    while True:
        print(x.xkblayout([], []))
        sleep(1)
