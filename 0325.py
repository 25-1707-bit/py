result = 0
def add(a, b):
    result = a + b
    print(result)

add(3,7)
add(3,9)
add(678,7)

def add(a, b, c):
    result = a + b + c
    return result

a = int(input("숫자 하나를 적으세요"))
b = int(input("숫자 하나를 적으세요"))
c = int(input("숫자 하나를 적으세요"))
result = add(a,b,c)
print (result)

def hello(a):
    print (a + " 안녕")

hello('홍길동')



def add(*args):
    result = 0
    for i in args:
        result = result + i
    result = result / len(args)
    return result

result = add(1,3,5,7,8,9)

print("가변 매개변수를 이용한 결과:", result)
