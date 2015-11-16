import requests
import json

curl --data 'query={"tags":["test1","test2"]}' http://www.test.com/match

payload = {'query': json.dumps({"tags":["test1", "test2"]})}
url = 'http://text-processing.com/api/sentiment/'

r = requests.post(url, data=payload)

if __name__=='__main__':
    print r.text


curl -d "text=great" http://text-processing.com/api/sentiment/

payload = "text=great"
url = "http://text-processing.com/api/sentiment/"
r =requests.post(url, d=payload)

print r.text