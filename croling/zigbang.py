import pandas as pd
import requests
import geohash2
def oneroom(addr):
    
    url = f'https://apis.zigbang.com/v2/search?leaseYn=N&q={addr}&serviceType=원룸'
    response = requests.get(url)
    data = response.json()['items'][0]
    lat, lng = data['lat'], data['lng']
    
    geohash = geohash2.encode(lat, lng, precision=5)
    
    url = f'https://apis.zigbang.com/v2/items/oneroom?\
geohash={geohash}&depositMin=0&rentMin=0&salesTypes[0]=전세&salesTypes[1]=월세\
&domain=zigbang&checkAnyItemWithoutFilter=true'
    response = requests.get(url)
    items = response.json()['items']
    ids = [item['itemId'] for item in items]
    
    url = 'https://apis.zigbang.com/v2/items/list'
    params = {'domain': 'zigbang', 'item_ids': ids[:900]}
    response = requests.post(url, params)
    items = response.json()['items']
    df = pd.DataFrame(items)
    df = df[df['address1'].str.contains(addr)].reset_index(drop=True)
    columns = ['item_id', 'address1', 'sales_type', 'deposit', 'rent', 'size_m2', 'title', 'manage_cost']
    return df[columns]
