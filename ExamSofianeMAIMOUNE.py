import time

def pump1():
    print("Executing pump 1")
    time.sleep(2)
    return 10

def pump2():
    print("Executing pump 2")
    time.sleep(3)
    return 20

def machine1(oil):
    print("Executing machine 1")
    time.sleep(5)
    return max(0, oil - 25), 1 if oil >= 25 else 0

def machine2(oil):
    print("Executing machine 2")
    time.sleep(3)
    return max(0, oil - 5), 1 if oil >= 5 else 0

def watchdog():
    oil = 0
    motor_count = 0
    wheel_count = 0
    while True:
        oil += pump1()
        oil += pump2()
        oil = min(50, oil)
        oil, motor = machine1(oil)
        motor_count += motor
        oil, wheel = machine2(oil)
        wheel_count += wheel
        print("Oil: ", oil)
        print("Motors: ", motor_count)
        print("Wheels: ", wheel_count)
        time.sleep(5)
        oil += pump1()
        time.sleep(15)
        oil += pump2()
        oil = min(50, oil)
        oil, motor = machine1(oil)
        motor_count += motor
        oil, wheel = machine2(oil)
        wheel_count += wheel
        print("Oil: ", oil)
        print("Motors: ", motor_count)
        print("Wheels: ", wheel_count)
        time.sleep(5)

if __name__ == "__main__":
    watchdog()
