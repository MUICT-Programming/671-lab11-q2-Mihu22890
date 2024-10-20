n = int(input())
lst = []

def summation(lst,n):
    sum_lst = []
    for i in range(n):
        sum = lst[0][i]+lst[1][i]
        sum_lst.append(sum)
    return sum_lst
    
def find_min_max(num):
    num_min = min(num)
    num_max = max(num)
    num_mm = (num_min, num_max)
    return num_mm
    
for i in range(2):
    lst_num = []
    for j in range(n):
        lst_num.append(int(input()))
    lst.append(lst_num)
num = summation(lst,n)
num_MM = find_min_max(num)
print(num)
print(num_MM)
