CPU temperature checker
-------------

Script for checking current CPU temperature or
average temperature in given time period.

You can get it by downloading it directly or by typing:

.. code:: bash

    $ pip install CPU_Temperature_Checker

After it is installed you can check your current temperature by running:

.. code:: bash

    $ get_current_cpu_temp

Or in case of expected excessive work of CPU, it is possible to monitor
CPU temperature in given time frame, after which you can find average value
of CPU temperature in a given time frame, inside a 'average_cpu_temperature.txt' file.

If temperature went over it's upper limit and reached critical level alert
sound will be raised and additional details will be found in 'critical_temperature_occurrences.txt'
file.

.. code:: bash

    $ get_average_cpu_temp 'integer value representing number of hours for which to monitor temperature of CPU'
