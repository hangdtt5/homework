# Cho một list A các điểm thi (từ 0-10) của các học viên trong lớp. Viết 3 hàm tính:

# giá trị trung bình (mean) của dãy.
# trung vị (median) của dãy A. trung vị là một số đứng ở vị trí giữa trong dãy số đã được sắp xếp theo thứ tự tăng dần, median chia dãy số cho trước thành 2 nửa bằng nhau. Nếu độ dài của dãy số là số lẻ, thì số ở giữa là median, nếu chiều dài của dãy số là số chẵn thì median được xác định bằng cách lấy trung bình của hai số ở giữa.
# mode của dãy A. Mode là phần tử có số lần xuất hiện nhiều nhất trong dãy. Mode sẽ giúp ta trả lời câu hỏi: "Trong lớp này, học viên đạt Điểm số nào nhiều nhất?".
# Lưu ý: kết quả trả ra sẽ là 1 list vì mode có thể nhiều hơn 1 giá trị.

# Vd:

# A = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10] ==> (mean(A), median(A), mode(A)) == (6.55, 7.0, [9])
# B=[4,4,5,4,5,5] thì (mean(B), median(B), mode(B)) == (4.5, 4.5, [4,5])

from collections import Counter
import operator

A = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
B = [4,4,5,4,5,5]

def index(X):
    mean = sum(X)/len(X)

    median = 0
    Y = sorted(X)
    if len(Y)%2 == 1:
        median = Y[int(len(X)/2)]
    else:
        median = (Y[int(len(X)/2 - 1)] +  Y[int(len(X)/2)])/2

    
    counts = Counter(X)
    max_count = max(counts.values())

    mode = []

    for p,count in counts.items():
        if count == max_count:
            mode.append(p)

    return mean, median, mode

print(index(A))
print(index(B))