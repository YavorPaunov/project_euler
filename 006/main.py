# author: Yavor Paunov

def sum_sq_diff(nums):
	sum_of_sq = sum([i**2 for i in range(1, nums+1)]);
	sq_of_sum = sum([i for i in range(1, nums+1)]) ** 2;
	return sq_of_sum - sum_of_sq;
	
if __name__ == "__main__":
	print(sum_sq_diff(100));