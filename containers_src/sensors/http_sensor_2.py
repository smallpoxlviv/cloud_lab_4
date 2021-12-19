import requests
import time
import os

sensor_id = 2
name = "river_2"
settlement = "settlement_2"
latitude = "12.1234567"
longtitude = "12.1234567"
water_level = 12

publish_url = os.environ.get("PUBLISH_URL")
timeout = int(os.environ.get("TIMEOUT"))

counter = 0
while True:
        counter+=1
        if counter >= 200:
                counter = 0
                x = random.uniform(0,1)
                if x > 0.5:
                        water_level+=1
                else:
                        water_level-=1
                if water_level <= 0 or water_level >= 20:
                        water_level = 12
                
        messageJson = '{"sensor_id": ' + str(sensor_id) + ',"name":"' + name + '","settlement": "' + settlement + '" ,"latitude": "' + latitude + '","longtitude": "' + longtitude + '" ,"water_level": ' + str(water_level) + '}'
        publish = requests.request('POST',publish_url ,data=messageJson)

        # print results
        print("Response status: ", str(publish.status_code))
        if publish.status_code == 200:
                print("Response body:", publish.text)
        time.sleep(timeout)