a = 10
b = 10
print(a is b)

a = 10000
b = 10000
print(a is b)

a = "hello"
b = "hello"
print(a is b)

a = "hellohellohel loehellohello"
b = "hellohellohel loehellohello"
print(a is b)

class A():
    a = 10000

class B():
    b = 10000

print(A.a is B.b)