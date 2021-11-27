import os
import sys

from fraction import Fraction


# Tạo class Fraction (phân số)

# Hàm khởi tạo nhận 2 giá trị nr (tử số) và dr (mẫu số)
# Nếu dr âm, chuyển dấu cho nr (VD: 1/-2 => -1/2)
# Triển khai phương thức phù hợp để in ra phân số (VD: print(fr) => -1/2)
# Viết hàm hcf tìm ước chung lớn nhất của nr và dr
# Thêm phương thức reduce rút gọn phân số (gọi trong _init_)
# Nếu nr == 0, chỉ in ra 0
# Nếu dr == 0, raise ZeroDevisonError
# Nếu dr == 1, chỉ in ra nr
# Triển khai các phương thức phù hợp cho phép +-*/ với 2 Fraction hoặc 1 Fraction với 1 số (int hoặc float), kết quả trả về 1 Fraction mới

print("\n\n")
fr1 = Fraction(0, 2)
fr2 = Fraction(1, 1)
fr3 = Fraction(2, 1)
fr4 = Fraction(1, 2)
other = Fraction(1.5, -3)
print(fr1, fr2, fr3, fr4, other)

print()

print(fr4 + other)
print(fr4 - other)
print(fr4 * other)
print(fr4 / other)

print()

fr = Fraction(1, 2)
print(fr + 1)
print(fr - 1.5)
print(fr * 2)
print(fr / 2)