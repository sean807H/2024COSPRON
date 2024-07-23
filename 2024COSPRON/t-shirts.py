def solution(shirt_size):
    # answer = []
    answer = [0] * 8
    # answer = [0 for _ in range(8)]
    unit = ["XS","S","M","L","XL","XXL","XXXL","XXXXL"]

    #카운팅
    for size in shirt_size:
        index = unit.index(size)        #index 는 리스트 함수만 해당
        answer[index] += 1

    return answer
shirt_size = ["XS","S","M","M","M","L","XL","XXL","XXXL","XXXXL"]
print(solution(shirt_size))