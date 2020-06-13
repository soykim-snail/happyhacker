import random
import requests
from pprint import pprint


numbers = range(1, 46)
pick = random.sample(numbers, 6)
print(pick)

lotto_url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=914'

response = requests.get(lotto_url)
print(response) # <Response [200]>
print(dir(response))
# ['__attrs__', '__bool__', '__class__', '__delattr__', 
# '__dict__', '__dir__', '__doc__', '__enter__', 
# '__eq__', '__exit__', '__format__', '__ge__', 
# '__getattribute__', '__getstate__', '__gt__', 
# '__hash__', '__init__', '__init_subclass__', 
# '__iter__', '__le__', '__lt__', '__module__', 
# '__ne__', '__new__', '__nonzero__', '__reduce__', 
# '__reduce_ex__', '__repr__', '__setattr__', 
# '__setstate__', '__sizeof__', '__str__', '__subclasshook__', 
# '__weakref__', '_content', '_content_consumed', 
# '_next', 'apparent_encoding', 'close', 'connection', 
# 'content', 'cookies', 'elapsed', 'encoding', 'headers', 
# 'history', 'is_permanent_redirect', 'is_redirect', 
# 'iter_content', 'iter_lines', 'json', 'links', 'next', 
# 'ok', 'raise_for_status', 'raw', 'reason', 
# 'request', 'status_code', 'text', 'url']

print(response.content)
# b'{"totSellamnt":89558503000,"returnValue":"success",
# "drwNoDate":"2020-06-06","firstWinamnt":1950005557,
# "drwtNo6":44,"drwtNo4":33,"firstPrzwnerCo":11,"drwtNo5":42,
# "bnusNo":27,"firstAccumamnt":21450061127,
# "drwNo":914,"drwtNo2":19,"drwtNo3":24,"drwtNo1":16}'

# json을 dictionary로 형변환
pprint(response.json()) 
# {'bnusNo': 27,
#  'drwNo': 914,
#  'drwNoDate': '2020-06-06',
#  'drwtNo1': 16,
#  'drwtNo2': 19,
#  'drwtNo3': 24,
#  'drwtNo4': 33,
#  'drwtNo5': 42,
#  'drwtNo6': 44,
#  'firstAccumamnt': 21450061127,
#  'firstPrzwnerCo': 11,
#  'firstWinamnt': 1950005557,
#  'returnValue': 'success',
#  'totSellamnt': 89558503000}
# print(type(response.json())) 

lotto_info = response.json()
bonus_num = lotto_info['bnusNo'] # 없는키면 error
bonus_num = lotto_info.get('bnusNo') # 없는키면 none
print('bonus_num :', bonus_num)

winner = []
for i in range(1, 7):
    lotto_num = lotto_info.get(f'drwtNo{i}')
    winner.append(lotto_num)
print(winner)

lotto_cnt = 0
for n in winner:
    for m in pick:
        if n == m:
            lotto_cnt += 1
print('lotto_cnt :', lotto_cnt)

bonus = False
for n in pick:
    if n == bonus_num:
        bonus = True
        break

if lotto_cnt == 6:
    print('1등입니다.')
elif lotto_cnt == 5:
    if bonus == True:
        print('2등입니다.')
else: 
    print('비당첨입니다.')


# set 사용하여 비교하기
match_num = set(pick) & set(winner)
print(match_num)
print(len(match_num))

