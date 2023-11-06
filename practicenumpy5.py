import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

y=numpy.sort(ages)
print(y)
print("Average is :",numpy.average(ages))
print("Median is :",numpy.median(ages))

x = numpy.percentile(ages, 75)
print(x)

print("percentile 50 is :",numpy.percentile(ages, 50))
print("percentile 60 is :",numpy.percentile(ages, 60))
print("percentile 70 is :",numpy.percentile(ages, 70))
print("percentile 75 is :",numpy.percentile(ages, 75))
print("percentile 80 is :",numpy.percentile(ages, 80))
print("percentile 90 is :",numpy.percentile(ages, 90))
print("percentile 95 is :",numpy.percentile(ages, 95))
print("percentile 100 is :",numpy.percentile(ages, 100))
