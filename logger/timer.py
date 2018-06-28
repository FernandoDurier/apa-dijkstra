import time

class Timer:
    
    def __init__(self):
        self.START = 0
        self.END = 0 
        self.DIFFERENCE = self.END - self.START

    def set_timer_start(self):
        self.START = int(round(time.time()*1000))
    
    def set_timer_end(self):
        self.END = int(round(time.time()*1000))

    def get_timer_start(self):
        return self.START

    def get_timer_end(self):
        return self.END
    
    def get_timer_difference(self):
        return self.END - self.START