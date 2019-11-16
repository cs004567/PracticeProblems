
import timeit

code_to_test = """
a = range(1000000)
b = [i*2 for i in a]
"""

elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)



