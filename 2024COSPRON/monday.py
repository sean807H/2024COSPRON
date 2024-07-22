#240722
scores = [2024, 7, 22, 3, 4]

#1
def sum_list(num):
    total = 0
    for i in num:
        total += i
    return total

print(sum_list(scores))   #2060

#2
def max_list(num1):
    # return max(num1)
    max_ = num1[0]
    for i in num1:
        if(i > max_):
            max_ = i
    return max_

print(max_list(scores))   #2024

#3
def min_list(num2):
    # return min(num2)
    min_ = num2[0]
    for i in num2:
        if(i < min_):
            min_ = i
    return min_

print(min_list(scores))   #3

#4
def average_list(num5):
    total = 0
    for i in num5:
        total += i
    return total/len(num5)

print(average_list(scores))   #412.0

#5
def count_odd(num3):
    count = 0
    for i in num3:
        if(i%2!=0):
            count+=1
    return count

print(count_odd(scores))   #10

#6
def make_list(num4):
    return [0] * num4

print(make_list(6))   #[0, 0, 0, 0, 0, 0]
