from cffi import FFI
from math import sqrt
from itertools import count, islice
from timeit import default_timer as timer

ffi = FFI()
cdef_from_file = None
headerFile = 'mylib.h'

with open(headerFile, 'r') as fin:
	cdef_from_file = fin.read()

ffi.cdef(cdef_from_file)
clib = ffi.dlopen('c_lib/libpy_c.so')

def testPrime_clib(testList):
	numInts = len(testList)
	data_in = ffi.new("int[]", testList)
	data_out = ffi.new("int[]", numInts)
	clib.getPrimes(data_in, numInts, data_out)
	data_out = ffi.unpack(data_out, numInts)
	return [d for i,d in enumerate(testList) if data_out[i]]

def testPrime_py(testList):
	def is_prime(n):
		return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n))))

	return [d for d in testList if is_prime(d)]


if __name__ == "__main__":
	testList = [17, 8191, 131071, 100000, 524287, 524289, 6700417, 6700419, 2147483647]

	print("Test list: {}\n".format(testList))
	num_iters = 100

	c_time = 0
	for i in range(1, num_iters+1):
		start = timer()
		res = testPrime_clib(testList)
		end = timer()
		c_time += end-start
	c_time /= num_iters
	print("Prime numbers returned by C:\n{}".format(res))
	print("Time taken by C: {} msecs\n".format(1000*c_time))

	py_time = 0
	for i in range(1, num_iters+1):
		start = timer()
		res = testPrime_py(testList)
		end = timer()
		py_time += end-start
	py_time /= num_iters
	print("Prime numbers returned by Python:\n{}".format(res))
	print("Time taken by Python: {} msecs\n".format(1000*py_time))
	print("--------------------------------------------------------")
	print("C code is {} times faster than Python".format(py_time/c_time))
	print("--------------------------------------------------------")