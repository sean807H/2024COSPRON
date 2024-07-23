# 할인가격 = 27000 = 가격 * 0.9 = 가격 * (1- 10/100)

unit = {"S":5, "G":10, "V":15}

def solution(price, grade):
    # unit에서 grade에 해당하는 값을 꺼내자
    rate = unit[grade]

    price = price * (1-rate/100)

    # if grade == "S":
    #     price = price * (1-5/100)
    # elif grade == "G":
    #     price = price * 0.9
    # elif grade == "V":
    #     price = price * (1-15/100)
    # answer = int(price)
    answer = price
    answer = int(answer)
    return answer
print(solution(2500,"G"))

