import httplib
import json


data = {
    "switch":"00:00:52:e6:8a:e9:c0:4a",
    "name":"flow_1_2",
    "cookie":"0",
    "priority":"32768",
    "in_port":"2",
    "eth_type":"0x0800",
    "active":"true",
    "eth_src":"02:b5:14:ae:ed:20",
    "eth_dst":"02:a7:76:8f:d2:ff",
    "ipv4_src":"10.0.0.1",
    "ipv4_dst":"10.0.0.2",
    "actions":"output=3"
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
