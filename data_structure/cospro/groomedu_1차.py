# 1
from abc import *
 
class DeliveryStore(metaclass=ABCMeta):
	@abstractmethod
	def set_order_list(self, order_list):
		pass

	@abstractmethod
	def get_total_price(self):
		pass
class Food:
	def __init__(self, name, price):
		self.name = name
		self.price = price

class PizzaStore():
	def __init__(self):
		menu_names = ["Cheese", "Potato", "Shrimp", "Pineapple", "Meatball"]
		menu_prices = [11100, 12600, 13300, 21000, 19500];
		self.menu_list = []
		for i in range(5):
			self.menu_list.append(Food(menu_names[i], menu_prices[i]))

		self.order_list = []

	def set_order_list(self, order_list):
		for order in order_list:
			self.order_list.append(order)

	def get_total_price(self):
		total_price = 0
		for order in self.order_list:
			for menu in self.menu_list:
				if order == menu.name:
					total_price += menu.price
		return total_price 

def solution(order_list):
	delivery_store = PizzaStore()

	delivery_store.set_order_list(order_list)
	total_price = delivery_store.get_total_price()
	return total_price


order_list = ["Cheese", "Pineapple", "Meatball"]
ret = solution(order_list)
 
print("solution 함수의 반환 값은", ret, "입니다.")

# 2
def func_a(string, length):
	padZero = ""
	padSize = length-len(string)
	for i in range(padSize):
		padZero += "0"
	return padZero + string

def solution(binaryA, binaryB):
	max_length = max(len(binaryA), len(binaryB))
	binaryA = func_a(binaryA, max_length)
	binaryB = func_a(binaryB, max_length)

	hamming_distance = 0
	for i in range(max_length):
		if binaryA[i] != binaryB[i]:
			hamming_distance += 1
	return hamming_distance

binaryA = "10010"
binaryB = "110"
ret = solution(binaryA, binaryB)

print("solution 함수의 반환 값은", ret, "입니다.")

# 3
def func_a(numA, numB, exp):
	if exp == '+':
		return numA + numB
	elif exp == '-':
		return numA - numB
	elif exp == '*':
		return numA * numB

def func_b(exp):
	for index, value in enumerate(exp):
		if value == '+' or value == '-' or value == '*':
			return index

def func_c(exp, idx):
	numA = int(exp[:idx])
	numB = int(exp[idx + 1:])
	return numA, numB
def solution(expression):
	exp_index = func_b(expression)
	first_num, second_num = func_c(expression, exp_index)
	result = func_a(first_num, second_num, expression[exp_index])
	return result

expression = "123+12"
ret = solution(expression)

print("solution 함수의 반환 값은", ret, "입니다.")

# 4
def solution(num):
	answer = num + 1

	while (str(answer).count("0") > 0):
		answer += 1

	return answer

num = 9949999
ret = solution(num)
 
print("solution 함수의 반환 값은", ret, "입니다.")

# 5
def solution(n):
	answer = 0
	arr = [[0] * n for _ in range(n)]
	dx = [1, 0, -1, 0]
	dy = [0, 1, 0, -1]

	num = 1
	arr[0][0] = num
	sx, sy = 0, 0

	while (num < n*n):
		for i in range(4):
			while (sx+dx[i] >= 0 and sx+dx[i] < n and sy+dy[i] >= 0 and sy+dy[i] < n and not arr[sx+dx[i]][sy+dy[i]]):
				sx, sy = sx+dx[i], sy+dy[i]
				num += 1
				arr[sx][sy] = num

	for i in range(n):
		answer += arr[i][i]

	return answer

n1 = 3
ret1 = solution(n1)

print("solution 함수의 반환 값은", ret1, "입니다.")
    
n2 = 2
ret2 = solution(n2)

print("solution 함수의 반환 값은", ret2, "입니다.")
