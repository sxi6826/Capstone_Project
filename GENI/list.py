import httplib
import json


data = {
    "switch":"00:00:52:e6:8a:e9:c0:4a",
    "name":"flow_mod_1",
    "cookie":"0",
    "priority":"32768",
    "in_port":"3",
    "eth_type":"0x0800",
    "active":"true",
    "eth_src":"02:a7:76:8f:d2:ff",
    "eth_dst":"02:b5:14:ae:ed:20",
    "ipv4_src":"10.0.0.2",
    "ipv4_dst":"10.0.0.1",
    "actions":"output=1"
    }
server = '128.82.75.97'
action = 'POST'
path = '/wm/staticentrypusher/list/all/json'
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