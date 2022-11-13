# write your code here!
# print('Meet a conicoin!')
import math
import requests
import json
# amount = float(input())
# print(f'I have {amount} conicoins.')
# print(f'{amount} conicoins cost {amount*100} dollars.')
# print('I am rich! Yippee!')
# e_rate = float(input('Please, enter the exchange rate: '))
# print(f'The total amount of dollars: {amount*e_rate}')

# convert = {'RUB': 2.98, 'ARS': 0.82, 'HNL': 0.17, 'AUD': 1.9622, 'MAD': 0.208}
#
# for key, value in convert.items():
#     print(f'I will get {round((value*amount),2)} {key} from the sale of {amount} conicoins.')

# currency = input()
#
# response = requests.get("https://floatrates.com/daily/"+currency+".json")
# if response.status_code != 200:
#     raise ConnectionError(response.status_code)
# data = response.json()
# print(data['usd'])
# print(data['eur'])
#
# print(data['usd']['rate'])
# print(data['eur']['rate'])
#
currency_i_have = str(input()).lower()

response = requests.get("https://floatrates.com/daily/"+currency_i_have+".json")
if response.status_code != 200:
    raise ConnectionError(response.status_code)
data = response.json()

# print(data['usd'])
# print(data['eur'])
rates = {}
if currency_i_have == 'usd':
    rates["eur"] = data["eur"]["rate"]
elif currency_i_have == 'eur':
    rates["usd"] = data["usd"]["rate"]
else:
    rates["usd"] = data["usd"]["rate"]
    rates["eur"] = data["eur"]["rate"]

# rates['usd'] = data["usd"]["rate"]
# rates['eur'] = data["eur"]["rate"]

while True:
    currency_i_want = input().lower()
    money_amount_i_have = float(input())
    if currency_i_want == '':
        break
    elif currency_i_want in rates:
        print('Checking the cache...')
        print("Oh! It is in the cache!")
        print(f'You received {round(money_amount_i_have * rates[currency_i_want], 2)} {currency_i_want.upper()}.')
    else:
        print('Checking the cache...')
        print('Sorry. but it is not in the cache!')
        rates[currency_i_have] = data[currency_i_have]['rate']
        print(f'You received {round(money_amount_i_have * rates[currency_i_want], 2)} {currency_i_want.upper()}.')

#
#
# import requests, json
#
# currency_current_code = str(input()).lower()
#
# url_current = f'http://www.floatrates.com/daily/{currency_current_code}.json'
#
# current_code = requests.get(url=url_current).json()
#
# cache = {}
# if currency_current_code == 'usd':
#     cache["eur"] = current_code["eur"]["rate"]
# elif currency_current_code == 'eur':
#     cache["usd"] = current_code["usd"]["rate"]
# else:
#     cache["usd"] = current_code["usd"]["rate"]
#     cache["eur"] = current_code["eur"]["rate"]
#
# while True:
#     receive = str(input()).lower() # currency user wants to receive
#
#     if receive == '':
#         break
#     elif receive in cache:
#         amount = float(input())
#         print("Checking the cache...")
#         print("Oh! It is in the cache!")
#         print(f"You received {round(amount * cache[receive], 2)} {receive.upper()}.")
#     else:
#         print("Checking the cache...")
#         print("Sorry, but it is not in the cache!")
#         amount = float(input())
#         print(f"You received {round(amount * current_code[receive]['rate'], 2)} {receive.upper()}")
#         cache[receive] = current_code[receive]['rate']
