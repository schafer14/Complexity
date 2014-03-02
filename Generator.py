def alpha_numeric_generator():
	num = 1;
	while True:
		for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
			yield letter + `num`
		num = num + 1

for thing in alpha_numeric_generator():
	print thing
