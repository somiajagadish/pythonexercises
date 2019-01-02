# Write your function below!
def fizz_count(x):
	count = 0
	for item in x:
		if item == "fizz":
			count = count + 1
	return count
  
s = fizz_count(["fizz","cat","fizz","fizz"])

print("the fizz count is " + str(s))
  