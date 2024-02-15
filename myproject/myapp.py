import requests
import json

URL="http://127.0.0.1:8000/info/"

data={'name':'BK','number':987462531,'city':'Maxi','pin_code':4212}

json_data=json.dumps(data)
r=requests.post(url=URL,data=json_data)
data=r.json()
print("========Json======",data)