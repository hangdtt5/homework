# Viết hàm có đầu vào là 1 chuỗi, trả ra số chữ cái, số ký tự viết hoa, số ký tự viết thường và số chữ số trong chuỗi đó. Giả sử đầu vào sau được cấp cho hàm:

# s = "Hello World! 123"

# Hàm count_char_type(s) sẽ trả ra 1 dict {"LETTERS":10, "CASE": {"UPPER CASE":2, "LOWER CASE":8}, "DIGITS":3}. Lưu ý: value của key "CASE" là một dict có 2 keys là "UPPER CASE", "LOWER CASE".

def count_char_type(s):
    letter = 0
    uppercase = 0
    lowercase = 0
    digit = 0
    mydict = {}
    for i in s:
        if i.isupper() == True:
            uppercase += 1
        elif i.islower() == True:
            lowercase += 1
        elif i.isdigit() == True:
            digit += 1
    letter = uppercase + lowercase
    return  {"LETTERS":letter, "CASE": {"UPPER CASE":uppercase, "LOWER CASE":lowercase}, "DIGITS":digit}

mystring = "Hello World! 123"
print(count_char_type(mystring))