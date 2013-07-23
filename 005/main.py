# author: Yavor Paunov

# A bit slow. Can be optimized further.
def even_div(max):
	smallest = max;
	while True:
		smallest += max;
		for i in range(1, max+1):
			if smallest % i > 0:
				break;
			elif i == max:
				return smallest;
			
if __name__ == "__main__":
	print(even_div(20));