import dateparser
import re


def day_diff(release_date, code_complete_day):
  # pip install dateparser
  days = (dateparser.parse(release_date, date_formats=['%d/%m/%Y']) - dateparser.parse(code_complete_day,
                                                                                       date_formats=['%Y-%m-%d']))
  return days.days


def alpha_num(data):
  words = data.split()
  alpha_num = list(filter(lambda x: x.isalnum() and re.findall('[0-9]', x), words))
  return alpha_num


def anagram_number(number):
  reversedNum = list(str(number))
  reversedNum.reverse()

  return int("".join(reversedNum)) == number


def roman_to_int(number):
  number = number.upper()
  nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
  sum = 0
  for i in range(len(number)):
    value = nums[number[i]]
    if i+1 < len(number) and nums[number[i+1]] > value:
      sum -= value
    else:
      sum += value
  return sum


if __name__ == '__main__':
  print("test_days = {}".format(day_diff("19/12/2021","2021-17-05"))) # 216
  print("test_days = {}".format(day_diff("10/05/2021","2021-01-03"))) # 70 dap an nay sai, thang 1-> 4 la hon 4 thang
  print(alpha_num("Emma25 is Data scientist50 and AI Expert"))  # ["Emma25", "scientist50"]
  print(alpha_num("tHE1 fOX iS cOMING2 fOR tHE4 cHICKEN"))  # ['tHE1', 'cOMING2', 'tHE4'])
  print(anagram_number(121121))
  print(anagram_number(1254))
  print(anagram_number(8888888888888888))
  print(roman_to_int("LVIII"))
  print(roman_to_int("IX"))
  print(roman_to_int("MCMXCIV"))
