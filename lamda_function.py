'''
def calculate(a,b):
    return a*a + 2*a*b + b*b

print(calculate(2,3))


#lamda parameter : expression
print((lambda a,b : a*a + 2*a*b + b*b) (2,3))


a = (lambda a,b : a*a + 2*a*b + b*b) (2,3)
print(a)
'''

#def cube(x):
    #return x*x*x
a = (lambda x : x*x*x) (2)
print(a)