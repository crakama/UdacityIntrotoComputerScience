# Write Python code to print out how far light travels
# in centimeters in one nanosecond.  Use the variables
# defined below.

speed_of_light = 299792458   # meters per second
centimeters = 100            # one meter is 100 centimeters
nanosecond = 1.0 / 1000000000  # one billionth of a second

# Speed = Distance/Time
time = 0.000000001
distance = 29979245800


def calcSpeed(time, distance):

    speed = distance / time   # cm per second
    print speed

calcSpeed(time, distance)
