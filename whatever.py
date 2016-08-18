def f08():
    total = 0
    for num in range(1, 501):
    	if num % 3 == 0 or num % 5 == 0:
    		total += num
    return total

print(f08())