class Generator():

	def alpha_numeric_generator(self, max=1000000):
		num = 1;
		while num < max:
			for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
				yield letter + `num`
			num = num + 1


