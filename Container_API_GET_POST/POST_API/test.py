import http.client
import json

conn = http.client.HTTPSConnection("getpantry.cloud")
payload = json.dumps({
  "id": "A1B2C3",
  "ime": "Marko",
  "prezime": "Markovic",
  "smer": "Informacione tehnologije",
  "predmeti": [
    "Veb dizajn",
    "Osnovi programiranja",
    "Matematika"
  ],
  "prosek": 8.5,
  "kontakt": {
    "adresa": "Makedonska 6",
    "telefon": 381615874844,
    "mesto": "Beograd"
  }
})
headers = {
  'Content-Type': 'application/json',
  'Cookie': '__cfduid=d039282c87fcafc8e2eb57b892f164d7b1619888018'
}
conn.request("POST", "/apiv1/pantry/3ab3757e-2586-4248-8cd5-843b30ae8ab8/basket/Student", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))