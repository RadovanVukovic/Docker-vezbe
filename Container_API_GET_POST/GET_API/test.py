import http.client
import json

conn = http.client.HTTPSConnection("getpantry.cloud")
payload = ''
headers = {}
conn.request("GET", "/apiv1/pantry/3ab3757e-2586-4248-8cd5-843b30ae8ab8/basket/Student", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))