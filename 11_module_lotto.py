import random
import requests

numbers = range(1, 46)
pick = random.sample(numbers, 6)
print(pick)

lotto_url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=914'

response = requests.get(lotto_url)
# print(dir(response))

# print(response.content)
# print(response.json()) # json을 dictionary로 형변환
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

