import requests

url = "<API-URL>"

payload = {}
headers = {
  'Authorization': 'Bearer <API_KEY>'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
