import httplib
import json


data = {
    "switch":"00:00:00:00:00:00:00:01",
    "name":"drop_1_4",
    "priority":"1067",
    "in_port":"1",
    "eth_src":"00:00:00:00:00:01",
    "eth_dst":"00:00:00:00:00:02",
    "ipv4_src":"10.0.0.1",
    "ipv4_dst":"10.0.0.2",
    "actions":"output:2"
    }

server = '127.0.0.1'
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
