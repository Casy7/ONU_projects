from random import randint
def list_of_primes_generator(max=1000):
	primes = [2]
	a = 2
	while a < max:
		counter = 0 
		for i in primes:
			if a % i == 0:
				counter += 1
		if counter == 0:
			primes.append(a)
		else:
			counter = 0
		a = a + 1
	return primes

first_file = "file1.txt"
second_file = "file2.txt"

primes = list_of_primes_generator()
with open (first_file,"w") as fst_file:
	for i in range(1000):
		fst_file.write(str(primes[randint(0,len(primes)-1)])+"\n")
with open (second_file,"w") as snd_file:
	for i in range(1000):
		snd_file.write(str(primes[randint(0,len(primes)-1)])+"\n")

with open (first_file) as fst_file:
	fst_values=[]
	for line in fst_file:
		int_line = int(line.replace("\n",""))
		fst_values.append(int_line)

with open (second_file) as snd_file:
	snd_values=[]
	for line in snd_file:
		int_line = int(line.replace("\n",""))
		snd_values.append(int_line)

first_set = set(fst_values)
second_set = set(snd_values)
first_set.intersection_update(second_set)
for i in first_set:
    print(i, end='; ')
