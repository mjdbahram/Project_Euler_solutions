import numpy as np 
import time

num = 10000
t0 = time.time()
multiples = np.arange(1, num)
print("sum of multiples of numbers under %d is %s, time:%f"%\
      (num, multiples[(multiples%3 == 0) + (multiples%5 == 0)].sum(), time.time()-t0))



