# Sorting - Sắp xếp điểm thi
# expand_more
# Điểm thi học kỳ của sinh viên được lưu ở định dạng 1 tuple có 3 phần tử (m1, m2, e) gồm:

# m1 = midterm1

# m2 = midterm2

# e = endterm

# Cho một list gồm danh sách điểm thi của sinh viên 1 lớp. Viết chương trình Python để sắp xếp danh sách trước theo thứ tự tăng dần theo phần tử cuối cùng trong mỗi tuple (sắp xếp theo điểm cuối kỳ - endterm tăng dần).

# vd sort_list_last([(1, 2, 5), (9, 1, 2), (6, 4, 4), (3, 2, 3), (10, 2, 1)]) == [(10, 2, 1), (9, 1, 2), (3, 2, 3), (6, 4, 4), (1, 2, 5)]

t = [(1, 2, 5), (9, 1, 2), (6, 4, 4), (3, 2, 3), (10, 2, 1)]
def sort_list_last(tuples):
  def last(n): return n[-1]
  return sorted(tuples, key=last)

print(sort_list_last(t))