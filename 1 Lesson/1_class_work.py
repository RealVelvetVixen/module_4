def strcounter(s):
	lits_counter = {}
	for lit in s:
		lits_counter[lit] = lits_counter.get(lit, 0) + 1

	for lit, counter in lits_counter.items():
		print(lit, counter)

strcounter("aksjjvva")