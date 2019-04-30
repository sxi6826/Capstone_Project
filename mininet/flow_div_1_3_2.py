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
    'switch':"00:00:00:00:00:00:00:01",
    "name":"flow_div_1_3_2",
    "cookie":"0",
    "priority":"32768",
    "in_port":"1",
    "eth_src":"00:00:00:00:00:01",
    "eth_dst":"00:00:00:00:00:03",
    "ipv4_src":"10.0.0.1",
    "ipv4_dst":"10.0.0.3",
    "active":"true",
    "eth_type":"0x0800",
    "actions":"set_eth_dst:00:00:00:00:00:02,set_ipv4_dst:10.0.0.2,output=2"
    }

pusher.set(flow1)
