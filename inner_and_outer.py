import numpy

in_a = list(map(int, input().split()))
in_b = list(map(int, input().split()))
a = numpy.array(in_a)
b = numpy.array(in_b)

print(numpy.inner(a, b))
print(numpy.outer(a, b))