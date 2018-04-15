import psutil
import datetime
import itertools
import time
import sys


class Sensor:

    def __iter__(self):
        return self

    def __next__(self):
        return psutil.sensors_temperatures()['k10temp'][0][1]


sensor = Sensor()
timestamp = iter(datetime.datetime.now, None)

degree_sign = u"\u00b0"


def get_current_cpu_temp():

    for stamp, value_in_c in itertools.islice(zip(timestamp, sensor), 1):
        value_in_f = value_in_c * 9/5 + 32
        print("{0}, {1} C{2}, {3} F{2}".format(stamp, value_in_c, degree_sign, value_in_f))


def average_temperature(hours=0, minutes=0):

    hours = int(hours)
    minutes = int(minutes)
    seconds = hours * 3600 + minutes * 60
    list_of_values_in_c = []
    list_of_values_in_f = []

    for stamp, value_in_c in itertools.islice(zip(timestamp, sensor), seconds):
        value_in_f = value_in_c * 9/5 + 32
        if value_in_c > psutil.sensors_temperatures()['k10temp'][0][3]:
            print('\a')
            with open("critical_temperature_occurrences.txt", 'a', encoding='utf-8') as g:
                g.write("CPU temperature hit a critically high value of {} C{} at {}\n".
                        format(value_in_c, degree_sign, stamp))
        list_of_values_in_c.append(value_in_c)
        list_of_values_in_f.append(value_in_f)
        time.sleep(1)

    average_temperature_in_celsius = round(sum(list_of_values_in_c)/len(list_of_values_in_c),2)
    average_temperature_in_fahrenheit = round(sum(list_of_values_in_f)/len(list_of_values_in_f),2)

    with open("average_cpu_temperature.txt", 'w', encoding='utf-8') as f:

        f.write("Average CPU temperature in the last {0} hours was: {1} C{3} ({2} F{3})\n".
                format(hours, average_temperature_in_celsius, average_temperature_in_fahrenheit, degree_sign))


def get_average_temperature():
    average_temperature(hours=sys.argv[1], minutes=sys.argv[2])


if __name__ == '__main__':
    get_current_cpu_temp()
    average_temperature(hours=1, minutes=30)

