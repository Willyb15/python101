def combos(numbers):
	combos = []
	for n1 in numbers:
		for n2 in numbers:
			if n1 != n2:
				combos.append((n1, n2))
	return combos
results = combos([3, 5, 8])
for result in results:
	print result
