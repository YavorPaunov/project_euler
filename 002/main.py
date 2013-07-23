
# A generator function for the Fibonacci sequence
def fib(max=10, cur=1, prev=0):
	yield cur;
	new = cur+prev;
	if new < max:
		for num in fib(max, new, cur):
			yield num;
	
if __name__ == "__main__":
	max = 4000000;
	# Use the genrotor to print the sum of all numbers divisible by 2
	print(sum([i for i in fib(4000000, 2, 1) if not i%2]));
