def avg(max, sets):
	return [((x)*sets+(float(sets-1)/2)) for x in range(max/sets)]


print avg(25, 5)