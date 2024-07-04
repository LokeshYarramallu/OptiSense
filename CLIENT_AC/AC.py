
import time


class AC:
    def __init__(self, temperature=24, fanspeed=1, root= None):
        self.temperature = temperature
        self.fanspeed = fanspeed
        self.fanspeed = fanspeed
        self.observers = [] 

        self.root = root
        self.temperature = 24
        self.fanspeed = 1

    def increase_temperature(self, diff =1):
        self.temperature = min(27, self.temperature+diff)
        self.adjust_fan_speed()

    def decrease_temperature(self, diff=1):
        self.temperature = max(16, self.temperature-diff)
        self.adjust_fan_speed()

    def increase_fanspeed(self):
        self.fanspeed = min(4,self.fanspeed+1)

    def decrease_fanspeed(self,):
        self.fanspeed = max(1,self.fanspeed-1)

    def get_temperature(self):
        return self.temperature

    def get_fanspeed(self):
        return self.fanspeed
    
    def get_status(self):
        status = f"status {self.get_temperature()} {self.get_fanspeed()} "
        return status

    def adjust_fan_speed(self):
        if self.temperature >= 22:
            self.fan_speed = 1
        elif 20 <= self.temperature < 22:
            self.fan_speed = 2
        elif 18 <= self.temperature < 20:
            self.fan_speed = 3
        elif self.temperature < 18:
            self.fan_speed = 4
