# author: Yavor Paunov

if __name__ == "__main__":
	max = 1000;
	
	total = sum([i for i in range(0, max, 3)]);
	total += sum([i for i in range(0, max, 5) if i%3 != 0]);
	
	print(total);