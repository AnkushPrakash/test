from string import ascii_letters
def twoSum(num,target):
    def helper(ind_one,ind_two):
        if ind_two == len(num):
            return helper(ind_one + 1, ind_one + 2)
        elif num[ind_one] >= target or num[ind_two] >= target:
            return helper(ind_one + 1, ind_two + 1)
        elif num[ind_one] + num[ind_two] == target:
            return (ind_one + 1, ind_two + 1)
        return helper(ind_one, ind_two + 1)
    return helper(0,0)

def majority(arr):
	length = len(arr);
	counts = {};
	for val in arr:
		if val in counts:
			counts[val] = counts[val] + 1;
		else:
			counts[val] = 1;
		if counts[val] > length / 2:
			return val


def excelHeader(string):
	x = {'A':1, 'B':2, 'C': 3}
	if string == "" or string is None:
		return 0;

	number = 0;
	for i in range(len(string)):
		number = number * 26;
		number += x[string[i]]
	return number;



def canJump(arr):
	if arr is [] or len(arr) == 1:
		return True;
	reached = False;
	for i in range(arr[0]):
		return reached or canJump(arr[i:])

def climbStairs(n):
	if n < 0:
		return 0
	elif n == 0:
		return 1
	return climbStairs(n - 1) + climbStairs(n - 2)

def all_anagrams(w):
    if w == "":
        return [""]
    anagrams = []
    for i in range(len(w)):
        subgrams = all_anagrams(w[0:i] + w[i + 1:])
        anagrams += [w[i] + s for s in subgrams]
    return anagrams







