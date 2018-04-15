"""
CPU temperature monitor
-------------

Script for checking current CPU temperature or
average temperature in given time period.

You can get it by downloading it directly or by typing:

    $ pip install CPU-temperature-monitor

After it is installed you can check your current temperature by running:

    $ get_current_cpu_temp

Or in case of expected excessive work of CPU, it is possible to monitor
CPU temperature in given time frame, after which you can find average value
of CPU temperature, inside a 'average_cpu_temperature.txt' file.

If temperature went over it's upper limit and reached critical level alert
sound will be raised and additional details will be stored in 'critical_temperature_occurrences.txt'
file.

    $ get_average_cpu_temp 'integer value representing number of hours' 'integer value representing number of minutes'

"""


from setuptools import setup

setup(name='CPU-temperature-monitor',
      version='0.1',
      description='Script for checking current CPU temperature or average temperature in given time period.',
      long_description=__doc__,
      long_description_content_type='text/markdown',
      url="https://github.com/urosjevremovic/CPU_temperature_checker",
      license='MIT',
      author='Uros Jevremovic',
      author_email='jevremovic.uros91@gmail.com',
      packages=['AvgCpuTemp'],
      install_requires=['psutil', ],
      entry_points={
          "console_scripts": ["get_current_cpu_temp=AvgCpuTemp.avg_cpu_temp:get_current_cpu_temp",
                              "get_average_cpu_temp=AvgCpuTemp.avg_cpu_temp:get_average_temperature"],
      },
      )

__author__ = 'Uros Jevremovic'
