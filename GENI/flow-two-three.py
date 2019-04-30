import httplib
import json


data = {
    "switch":"00:00:52:e6:8a:e9:c0:4a",
    "name":"flow_2_3",
    "cookie":"0",
    "priority":"32768",
    "in_port":"3",
    "eth_type":"0x0800",
    "active":"true",
    "eth_src":"02:a7:76:8f:d2:ff",
    "eth_dst":"02:69:0d:03:19:ef",
    "ipv4_src":"10.0.0.2",
    "ipv4_dst":"10.0.0.3",
    "actions":"output=1"
    }

server = '128.82.75.97'
action = 'POST'
path = '/wm/staticentrypusher/json'
headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            }
body = json.dumps(data)
conn = httplib.HTTPConnection(server, 8080)
conn.request(action, path, body, headers)
response = conn.getresponse()
ret = (response.status, response.reason, response.read())
print ret
conn.close()
