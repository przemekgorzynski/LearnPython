#!/usr/bin/env python3
# Requires speedtest-cli library
import json
import speedtest


# Poland,Warsaw,Powszechna Agencja Informacyjna S.A.,14781

def test_speed():
    s = speedtest.Speedtest(secure=True)
    s.get_servers()
    s.download()
    s.upload()
    res = s.results.dict()
    return res

def prepare_json(x):
    output = {}
    output["Date"] = x["timestamp"].split("T")[0]
    output["Time"] = x["timestamp"].split("T")[1].split(".")[0]
    output["Server"] = x["server"]["name"]
    output["Ping"] = x["ping"]
    output["Download Mbit/s"] = round(x["download"] / 1000 / 1000, 1)
    output["Upload Mbit/s"] = round(x["upload"] / 1000 / 1000, 1)
    return output

raw_data=test_speed()
json_data=prepare_json(raw_data)

with open('./json_data.json', 'a') as outfile:
    json.dump(json_data, outfile)
    outfile.write('\n')
