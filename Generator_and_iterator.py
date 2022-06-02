#Creating a generator
def gencubes(n):
    for nun in range(n):
        yield nun **3

for x in gencubes(10):
    print(x)

#Similar function without generator
def gencubes2(n):
    lst = []
    for num in range(n):
        lst+=[num**3]
    return lst
print(gencubes2(10))

#New example Fibonacci
def genfib(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b, a + b

for num in genfib(10):
    print(num)

print(list(genfib(10)))


#New example Fibonacci 2
def fib2(n):
    a = 1
    b = 1
    output = []

    for i in range(n):
        output += [a]
        a,b=b,a+b
    return output

print(fib2(10))

#using next()
g = genfib(5)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

#using iter
s = 'Hello'
for char in s:
    print(char)

#next(s) can't e used

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))


