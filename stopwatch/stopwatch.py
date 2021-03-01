import time

class Stopwatch:
    def __init__(self):
        self.start_time = 0
        self.paused_counter = 0
        self.total = []

    def StartTimer(self):
        self.start_time = time.time()
    
    def GetDuration(self) -> int:
        return self.stopped_time - self.start_time
    
    def StopTimer(self):
        self.stopped_time = time.time()
    
    def PauseTimer(self):
        self.paused_counter += 1
        self.total.append(time.time() - self.start_time)
        
    def GetNumberOfPauses(self) -> int:
        return self.paused_counter
    
    def get_lap_times(self):
        string = ""
        for num,x in enumerate(self.total):
            string += f"{num} : {x}\n"
        return string.rstrip()
    




a = Stopwatch()
for x in range(6):
    a.StartTimer()
    n = 2
    for x in range(1000000):
        v = n * x
        n = v
    a.PauseTimer()

b = a.get_lap_times()

print(b)
