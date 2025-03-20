import pytest
from Timer import Timer

def test_timer_constructor():
    timer = Timer()
    assert timer.elapsed_time == 0
    assert timer.running == False

def test_timer_start():
    timer = Timer()
    timer.start()
    assert timer.running == True
    assert timer.elapsed_time == 0

def test_timer_start_error():
    timer = Timer()
    timer.start()
    with pytest.raises(RuntimeError):
        timer.start()

def test_timer_tick():
    timer = Timer()
    timer.start()
    timer.tick()
    assert timer.elapsed_time == 1
    timer.tick()
    assert timer.elapsed_time == 2

def test_timer_tick_not_running():
    timer = Timer()
    assert timer.tick() == False

def test_timer_get_time():
    timer = Timer()
    timer.start()
    timer.tick()
    assert timer.get_time() == 1

def test_timer_str():
    timer = Timer()
    timer.start()
    timer.tick()
    assert str(timer) == "Elapsed time: 1 seconds"

def test_timer_eq():
    timer1 = Timer()
    timer1.start()
    timer1.tick()
    timer1.tick()
    timer2 = Timer()
    timer2.start()
    timer2.tick()
    timer2.tick()
    assert timer1 == timer2

def test_timer_eq_error():
    timer1 = Timer()
    with pytest.raises(TypeError):
        timer1 == 5


