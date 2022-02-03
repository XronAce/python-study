import requests # If this code throws 'no module' error, do 'pip install requests' on your console.
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

diff = int(btc['max_price']) - int(btc['min_price'])
stNum = int(btc['opening_price']) + diff

if stNum > int(btc['max_price']):
    print("상승장")
else:
    print("하락장")