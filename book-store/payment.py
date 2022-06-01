import json
import requests

# Anonymous test key. Replace with your key.
SECRET_KEY = 'sk_test_960bfde0VBrLlpK098e4ffeb53e1'

response = requests.post(
  'https://online.yoco.com/v1/charges/',
  headers={
    'X-Auth-Secret-Key': SECRET_KEY,
  },
  json={
    'token': 'tok_test_DjaqoUgmzwYkwesr3euMxyUV4g',
    'amountInCents': 2799,
    'currency': 'ZAR',
  },
)

# response.status_code will contain the HTTP status code
# response.json() will contain the response body
