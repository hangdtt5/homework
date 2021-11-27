import os
import sys

from bank_account import BankAccount
from customer import Customer
from saving_account import SavingAccount
from bank_account2 import BankAccount2

# Khai báo class SavingAccount kế thừa từ BankAccount, bổ sung:
# monthly_interest_rate: Lãi suất hàng tháng = 0.005
# calculate_interest(): tính tiền lãi hàng tháng, công thức balance * monthly_interest_rate
# Tạo class Customer bao gồm một số thông tin:
# name, date_of_birth, email, phone
# get_info() hiển thị thông tin Customer
# Thay đổi class BankAccount:
# account_name thành owner là một Customer
# display() hiển thị thông tin số tài khoản, thông tin khách hàng và số dư

# Thay đổi các thuộc tính account_number, account_name, balance trong class BankAccount thành thuộc tính ẩn, và triển khai thêm các phương thức:

# get_account_number()
# get_account_name()
# get_balance()
# set_balance() - balance phải lớn hơn hoặc bằng 0
# Thay đổi các phương thức display(), withdraw() và deposit() sử dụng các phương thức getter và setter trên.

# Chú ý:

# Với withdraw(), amount phải lớn hơn 0 và nhỏ hơn balance
# Với deposit(), amount phải lớn hơn 0
# Nếu giá trị không phù hợp thì thông báo ra console

cus = Customer("HangDTT","9/1/1984","hangdtt@gmail.com","090832432432")
bank_account = SavingAccount("000580370002", cus, 1000000) 
bank_account.display() 

print ("Lãi suất: {}".format(bank_account.calculate_interest()))



# Bổ sung thêm phương thức from_json cho class BankAccount để nạp dữ liệu từ file JSON

# Đầu vào là đường dẫn file JSON (lưu ý xử lý path)
# Kết quả trả về là một list accounts
# Sử dụng vòng lặp, in list theo dạng bảng
# Triển khai thêm phương thức magic method phù hợp để in ra với hàm print
current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
json_file = os.path.join(current_dir, "bank_accounts.json")
json_accounts = BankAccount2.from_json(json_file)

print("\n\n")
print(f"| {'Number':9} | {'Account Name':15} | {'Balance':15} |")
print(f"|{'-' * 11}|{ '-' * 17 }|{'-' * 17}|")
for account in json_accounts:
    account.display()


