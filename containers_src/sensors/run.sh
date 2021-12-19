#!/bin/bash

exec python3 /sensors/cloud_lab_4/containers_src/sensors/http_sensor_1.py &
exec python3 /sensors/cloud_lab_4/containers_src/sensors/http_sensor_2.py &
exec python3 /sensors/cloud_lab_4/containers_src/sensors/http_sensor_3.py