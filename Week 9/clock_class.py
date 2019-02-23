class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return 'The time is {}:{}:{}'.format(self.hours, self.minutes, self.seconds)

timer = Clock(2,40,55)

print(timer)