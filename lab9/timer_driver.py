"""
File: parkiest_neighbourhood_driver.py
Author:  Weijian Zhao (David)
Date: 2025-02-19
Class: CS_5001, Spring_2025
"""
from Timer import Timer
import time


def main():
    """
    The main function that tests the Timer class.
    """
    timer1 = Timer()
    timer1.start()
    number_of_ticks = 5
    print("Timer started...")
    for _ in range(number_of_ticks):
        timer1.tick()
        print(timer1)
        time.sleep(1)
    print(f"Total elapsed time after {number_of_ticks} tick\
          s: {timer1.get_time()} second(s)")
    print(f"Final timer status: {timer1}")
    timer2 = Timer()
    timer2.start()
    for _ in range(10):
        timer2.tick()
        print(timer2)
        time.sleep(1)
    print(f"Total elapsed time after {number_of_ticks} tick \
          s: {timer2.get_time()} second(s)")
    print(f"Final timer status: {timer2}")


if __name__ == "__main__":
    main()
