def greater_less_equal_5(answer):
	print("answer value = " + str(answer))
	if answer > 5:
		return 1
	elif answer < 5:          
		return -1
	else:
		return 0
        
print(str(greater_less_equal_5(4)))
print(str(greater_less_equal_5(5)))
print(str(greater_less_equal_5(6)))
