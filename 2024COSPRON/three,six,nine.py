# def solution(number):
# 	count = 0
# 	for i in range(1, number + 1):
# 		current = i
# 		while current != 0:
# 			if :
# 				count += 1
# 			current = current // 10
# 	return count

def solution2(number):
    count = 0
    for number in range(1, number+1):
        number_str = str(number)
        count += number_str.count("3")
        count += number_str.count("6")
        count += number_str.count("9")
        # for s in number_str:
        #     if s in "369" :
        #         count += 1
    return count

number = 40
ret = solution2(number)

print("solution 함수의 반환 값은", ret, "입니다.")