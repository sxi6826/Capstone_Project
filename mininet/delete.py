import httplib
import json
n = (raw_input("Enter the name of flow to delete"))

data = {
    "name":n
    }
server = '128.82.75.97'
action = 'DELETE'
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
