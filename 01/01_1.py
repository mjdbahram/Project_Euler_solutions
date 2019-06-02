import time

num = 10000
multiples = []

t0 = time.time()
for i in range(num):
	if (i%3 == 0 or i%5== 0):
		multiples.append(i)

print("sum of multiples of numbers under %d is %s, time:%f"%(num, sum(multiples),time.time()-t0))


