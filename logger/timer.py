import time

class Timer:
    
    def __init__(self):
        self.START = 0
        self.END = 0 
        self.DIFFERENCE = self.END - self.START

    def set_timer_start(self):
        self.START = time.time()
    
    def set_timer_end(self):
        self.END = time.time()

    def get_timer_start(self):
        return self.START

    def get_timer_end(self):
        return self.END
    
    def get_timer_difference(self):
        return self.DIFFERENCE