import requests
from pprint import pprint


def mask(address, n=10):
    print(address, n)
    URL = '	https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json'
    params = f'?address={address}'
    response = requests.get(URL+params)

    # print(URL+params)
    # print(response.json()) # dictionary로 형변화
    stores = response.json().get('stores')[:n]
    # print(stores)

    for store in stores:
        # pprint(store)    
        if store.get('remain_stat') == 'plenty':
            color = 'green'
        elif store.get('remain_stat') == 'some':
            color = 'yellow'
        elif store.get('remain_stat') == 'few':
            color = 'red'
        else:
            color ='gray'
        print(store.get('name'), color)