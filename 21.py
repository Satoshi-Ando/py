# coding: utf-8

#def double(x):
#    return x * x
#print map(double, [2, 5, 8])

print map(lambda x: x * x, [2, 5, 8])

def double(x):
    print x * x
double(3)
