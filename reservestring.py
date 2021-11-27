# Xử lý chuỗi - Đảo ngược từ và kiểu hoa thường
# expand_more
# Cho 1 chuỗi A (vd: "tHE fOX iS cOMING fOR tHE cHICKEN"). Viết hàm đảo ngược thứ tự các từ trong chuỗi và đổi tất cả các chữ cái từ hoa thành thường và ngược lại. (kết quả là "Chicken The For Coming Is Fox The")

s= str(input("Nhập chuỗi: ")) 
def reserve_string(s):
    split_str = s.split()
    join_str = ' '.join(split_str[::-1])
    print(join_str.swapcase())
reserve_string(s)