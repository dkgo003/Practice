### 10998번
# https://www.acmicpc.net/problem/10998

A, B = input().split()
A = int(A)
B = int(B)
print(A*B) 

### 1008번
# https://www.acmicpc.net/problem/1008

A, B = input().split()
A = int(A)
B = int(B)
print(A/B) 

### 10926번
# https://www.acmicpc.net/problem/10926

name = input()
print(f'{name}??!')

### 18108번
# https://www.acmicpc.net/problem/18108

y = input()
y = int(y)
print(f'{y-543}')

### 10430번
# https://www.acmicpc.net/problem/10430

A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)

### 2588번
# https://www.acmicpc.net/problem/2588

a = input()
a = int(a)
b = input()
res = []
for i in b:
    i = int(i)
    res.append(i)
print(a*res[2])
print(a*res[1])
print(a*res[0])
print(a*int(b))

### 11382번
# https://www.acmicpc.net/problem/11382

A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
print(A+B+C)

### 10171번
# https://www.acmicpc.net/problem/10171

print('\\    /\\')
print(" )  ( ')")
print('(  /  )')
print(' \(__)|')

### 10172번
# https://www.acmicpc.net/problem/10172

print('|\\_/|')
print('|q p|   /}')
print('( 0 )"""\\')
print('|"^"`    |')
print('||_/=\\\\__|')

### 1330번
# https://www.acmicpc.net/problem/1330

A, B = input().split()
A = int(A)
B = int(B)
if A>B:
    print('>')
elif A<B:
    print('<')
elif A==B:
    print('==')

### 9498번
# https://www.acmicpc.net/problem/9498

num = int(input())
if (90<=num)&(num<=100):
    print('A')
elif (80<=num)&(num<90):
    print('B')
elif (70<=num)&(num<80):
    print('C')
elif (60<=num)&(num<70):
    print('D')
else:
    print('F')