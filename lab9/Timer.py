'''
File: Timer.py
Author:  Weijian Zhao (David)
Date: 2025-03-12
Class: CS_5001, Spring_2025
'''


class Timer:
    def __init__(self):
        """
        Constructor
        Initializes the timer with an elapsed time 
        of 0 seconds and a running status of False.
        """
        self.elapsed_time = 0
        self.running = False

    def start(self):
        """
        Starts the timer by setting the running status
          to True and resets the elapsed time to 0.
        """
        if self.running:
            raise RuntimeError("Timer is already running.")
        self.elapsed_time = 0
        self.running = True

    def tick(self):
        """
        Simulates the passage of one second.
        If the timer is running, it increments elapsed_time by 1.
        """
        if not self.running:
            return False
        self.elapsed_time += 1
        return True

    def get_time(self):
        """
        Returns the total elapsed time in seconds.
        """
        return self.elapsed_time

    def __str__(self):
        """
        Returns a string representation of the Timer object.
        """
        return f"Elapsed time: {self.elapsed_time} seconds"

    def __eq__(self, other):
        """
        Compares two Timer objects and returns True 
        if their elapsed_time is the same.
        Otherwise, it returns False.
        """
        if not isinstance(other, Timer):
            raise TypeError("Comparing object must be of type Time.")
        return self.elapsed_time == other.elapsed_time


if __name__ == "__main__":  # pragma: no cover
    timer1 = Timer()
    timer1.start()
    timer1.tick()
    timer1.tick()
    print(timer1)
    print(timer1.get_time())
    timer2 = Timer()
    timer2.start()
    timer2.tick()
    timer2.tick()
    print(timer2)
    print(timer2.get_time())
