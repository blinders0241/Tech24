import os,json,requests
import urllib.parse
import datetime

class initiateRequest:
        # Your existing code...
    def __init__(self):
        self.headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'DNT': '1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
            'Sec-Fetch-User': '?1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'navigate',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
        }
        self.curl_headers = ''' -H "authority: beta.nseindia.com" -H "cache-control: max-age=0" -H "dnt: 1" -H "upgrade-insecure-requests: 1" -H "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36" -H "sec-fetch-user: ?1" -H "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9" -H "sec-fetch-site: none" -H "sec-fetch-mode: navigate" -H "accept-encoding: gzip, deflate, br" -H "accept-language: en-US,en;q=0.9,hi;q=0.8" --compressed'''
        self.run_time = datetime.datetime.now()
        # self.con = DbConnections().connectToDB()

    
    def establishVPNConnection(self,payload):
        if (("%26" in payload) or ("%20" in payload)):
            encoded_url = payload
        else:
            encoded_url = urllib.parse.quote(payload, safe=':/?&=')
        payload_var = 'curl -b cookies.txt "' + encoded_url + '"' + self.curl_headers + ''
        try:
            output = os.popen(payload_var).read()
            output=json.loads(output)
        except ValueError:  # includes simplejson.decoder.JSONDecodeError:
            payload2 = "https://www.nseindia.com"
            output2 = os.popen('curl -c cookies.txt "'+payload2+'"'+ self.curl_headers+'').read()
    
            output = os.popen(payload_var).read()
            establishVPNConnection=json.loads(output)
        return establishVPNConnection
    
    def establishConnection(self,payload):
        try:
            output = requests.get(payload,headers=self.headers).json()
            print(output)
        except ValueError:
            s =requests.Session()
            output = s.get("http://nseindia.com",headers=self.headers)
            establishConnection = s.get(payload,headers=self.headers).json()
        return establishConnection