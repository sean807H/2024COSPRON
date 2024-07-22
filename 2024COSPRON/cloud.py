#240722
scores = [27, 17, 7, 21, 30, 3, 45, 5, 53, 1001, 26, 62, 559]

#합계
def sum_list(scores):
    sum_ = 0
    for score in scores:
        sum_ += score
    return sum_

print(sum_list(scores))

def sum_list2(scores):
    sum_ = 0
    for i in range(len(scores)):
        sum_ += scores[i]
    return sum_

print(sum_list2(scores))

def sum_list3(scores):
    return sum(scores)

print(sum_list3(scores))

#최댓값
def max_list(scores):
    max_ = scores[0]
    for i in scores:
        if i > max_ :
            max_ = i
    return max_

print(max_list(scores))

def max_list2(scores):
    max_ = scores[0]
    for i in range(1, len(scores)):
        if scores[i] > max_ :
            max_ = scores[i]
    return max_

print(max_list2(scores))

def max_list3(scores):
    return max(scores)

print(max_list3(scores))

#최솟값
def min_list(scores):
    min_ = scores[0]
    for i in scores:
        if i < min_ :
            min_ = i
    return min_

print(min_list(scores))

def min_list2(scores):
    min_ = scores[0]
    for i in range(len(scores)):
        if scores[i] < min_:
            min_ = scores[i]
    return min_

print(min_list2(scores))

def min_list3(scores):
    return min(scores)

print(min_list3(scores))

#평균
def average_list(scores):
    total = 0
    for i in scores:
        total += i
    return total/len(scores)

print(average_list(scores))

def average_list2(scores):
    return sum(scores) / len(scores)

print(average_list2(scores))

#홀수
def count_odd(scores):
    count = 0
    for i in scores:
        if i%2!=0:
            count+=1
    return count

print(count_odd(scores))

def count_odd2(scores):
    count = 0
    for i in range(len(scores)):
        if scores[i]%2!=0 :
            count+=1
    return count

print(count_odd2(scores))

def count_odd3(scores):
    odd_list = [score for score in scores if score % 2 == 1]
    return len(odd_list)

print(count_odd3(scores))

#N개의 리스트
def make_list(scores):
    list_ = []
    for _ in scores:
        list_.append(0)
    return list_

print(make_list(scores))

def make_list2(scores):
    list_ = []
    for _ in range(len(scores)):
        list_.append(0)
    return list_

print(make_list2(scores))

def make_list3(scores):
    list_ = [0 for _ in scores]
    return list_

print(make_list3(scores))

def make_list4(scores):
    return [0] * len(scores)

print(make_list4(scores))