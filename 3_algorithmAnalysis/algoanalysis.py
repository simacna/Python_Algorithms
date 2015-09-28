# We are interested in characterizing an algorithm's running time as a function of the input size.

# 3.1 - Experimental studies

from time import time
start_time = time()
run algorithm
end_time = time()
elapsed = end_time - start_time

# Because many processes share use of a computer central processing unit (CPU), the elapsed time will depend on what other
# processes are running on the computer when the test is performed. 
# A fairer metric is the number of CPU cycles that used by the algorithm. This can be determined using the clock function of the time
# module, but even this measure might not be consistent if repeating the identical algo on the identical input. 