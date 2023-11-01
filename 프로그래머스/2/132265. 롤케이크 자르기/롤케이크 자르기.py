from collections import Counter

def solution(toppings):
    answer = 0
    A, B = set(), Counter(toppings) # 토핑의 종류
    a, b = 0, len(B) # 토핑의 개수
    for topping in toppings:
        B[topping] -= 1
        
        if B[topping] == 0:
            b -= 1 
        
        if topping not in A:
            A.add(topping)
            a += 1

        if a == b:
	        answer += 1
        
        if a > b:
	        break
        
    return answer