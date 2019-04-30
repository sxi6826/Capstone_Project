import httplib
import json

data1 = {
    "src-ip": "10.0.0.1/32",
    "dst-ip": "10.0.0.2/32",
    "actions": "allow"
}

data2 = {
    "src-ip": "10.0.0.2/32",
    "dst-ip": "10.0.0.3/32",
    "actions": "deny"
}

data3 = {
    "src-ip": "10.0.0.3/32",
    "dst-ip": "10.0.0.1/32",
    "actions": "deny"
}

server = '128.82.75.97'
action = 'POST'
path = '/wm/acl/rules/json'
headers = {
    'Content-type': 'application/json',
    'Accept': 'application/json',
}
body = json.dumps(data1)
conn = httplib.HTTPConnection(server, 8080)
conn.request(action, path, body, headers)
response = conn.getresponse()
ret = (response.status, response.reason, response.read())
print ret
conn.close()

body = json.dumps(data2)
conn = httplib.HTTPConnection(server, 8080)
conn.request(action, path, body, headers)
response = conn.getresponse()
ret = (response.status, response.reason, response.read())
print ret
conn.close()

body = json.dumps(data3)
conn = httplib.HTTPConnection(server, 8080)
conn.request(action, path, body, headers)
response = conn.getresponse()
ret = (response.status, response.reason, response.read())
print ret
conn.close()
