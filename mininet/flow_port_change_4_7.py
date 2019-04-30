import httplib
import json

class StaticFlowPusher(object):

    def __init__(self, server):
        self.server = server

    def get(self, data):
        ret = self.rest_call({}, 'GET')
        return json.loads(ret[2])

    def set(self, data):
        ret = self.rest_call(data, 'POST')
        return ret[0] == 200

    def remove(self, objtype, data):
        ret = self.rest_call(data, 'DELETE')
        return ret[0] == 200

    def rest_call(self, data, action):
        path = '/wm/staticflowpusher/json'
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            }
        body = json.dumps(data)
        conn = httplib.HTTPConnection(self.server, 8080)
        conn.request(action, path, body, headers)
        response = conn.getresponse()
        ret = (response.status, response.reason, response.read())
        print ret
        conn.close()
        return ret

pusher = StaticFlowPusher('127.0.0.1')

flow1 = {
    'switch':"00:00:00:00:00:00:00:02",
    "name":"flow_port_change_4_7",
    "cookie":"0",
    "priority":"32768",
    "in_port":"1",
    "eth_src":"00:00:00:00:00:04",
    "eth_dst":"00:00:00:00:00:07",
    "ipv4_src":"10.0.0.4",
    "ipv4_dst":"10.0.0.7",
    "tp_dst":"5000",
    "eth_type":"0x0800",
    "actions":"set_tp_dst:6000,output=3"
    }

pusher.set(flow1)
