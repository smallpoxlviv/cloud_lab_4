import awsgi
import sys
import pymysql
import json
from datetime import datetime
from pytz import timezone, common_timezones
import pytz
import time
import os
from flask_cors import CORS
from flask import Flask, jsonify, request


#rds settings
rds_host  = "lab2database.chov87qbwh0h.eu-central-1.rds.amazonaws.com"
name = os.environ.get("db_username")
password = os.environ.get("db_password")
db_name = os.environ.get("db_name")
    
sensor_id_key = "sensor_id"
name_key = 'name'
settlement_key = 'settlement'
latitude_key = "latitude"
longtitude_key = "longtitude"
water_level_key = "water_level"

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*", "allow_headers": "*", "expose_headers": "*"}})
BASE_ROUTE = "/iot"

@app.route(BASE_ROUTE, methods=["GET"])
def get_river():
    try:
        conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    except pymysql.MySQLError as e:
        return jsonify({"body" : "MySQLError"})

    data = []
    with conn.cursor() as cur:
        cur.execute("select * from river;")
        rows = cur.fetchall()
        for row in rows:
            row_dict = {
                'id': row[0],
                'sensor_id': row[1],
                'name': row[2], 
                'settlement': row[3], 
                'latitude': str(row[4]),
                'longtitude': str(row[5]),
                'water_level': row[6],
                'measurement_date': str(row[7])
            }
            data.append(row_dict)
    conn.commit()

    return jsonify({"body" : json.dumps(data)})


@app.route(BASE_ROUTE, methods=["POST"])
def add_river():

    try:
        conn = pymysql.connect(host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    except pymysql.MySQLError as e:
        return jsonify({"body" : "MySQLError"})

    sensor_id = request.json[sensor_id_key]
    name = event[state_key][reported_key][name_key]
    settlement = event[state_key][reported_key][settlement_key]
    latitude = event[state_key][reported_key][latitude_key]
    longtitude = event[state_key][reported_key][longtitude_key]
    water_level = event[state_key][reported_key][water_level_key]

    ts = time.time()
    my_time = datetime.fromtimestamp(ts,tz=pytz.utc)
    tz1 = pytz.timezone('US/Eastern')
    xc = my_time.astimezone(tz1)
    measurement_date = xc.strftime("%Y-%m-%d %H:%M:%S")

    data = [{
        "sensor_id": sensor_id,
        "name": name,
        "settlement": settlement,
        "latitude": latitude,
        "longtitude": longtitude,
        "water_level": water_level,
        "measurement_date": measurement_date
    }]

    with conn.cursor() as cur:
        sql = "UPDATE `river` SET name=%s, settlement=%s, latitude=%s, longtitude=%s,\
         water_level=%s, measurement_date=%s WHERE sensor_id=%s LIMIT 1;"
        cur.execute(sql, (name, settlement, latitude, longtitude, water_level, measurement_date, sensor_id))
    conn.commit()

    return jsonify({"body" : json.dumps(data)})
    

@app.route(BASE_ROUTE + "/healthcheck", methods=["GET"])
def healthcheck():
    return jsonify({"body" : json.dumps(data)})


def handler(event, context):
    return awsgi.response(app, event, context)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
