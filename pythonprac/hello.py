print('Hello World')

# var / calc
a=2
b=3
print(a+b)

a1='하'
a2='에'
print(a1+a2)

b1='1'
b2='2'
print(b1+b2)

c1=123.33
c2=52/5
print(c1/c2)

# list
c = ['사과', '배', '감']
print(c[0])

# dictionary {'key':'value'} , ...
d = {'name':'영수', 'age':'24'}
print(d['name'])

# 함수 사용
# javascript에선
# function hey(){
#   alert('hey!')
# }
# 처럼 표현했었다.
# python에서는? 중괄호X ****(콜론+엔터하면 탭이생긴다. 탭없으면 안됨)***을 사용한다.
def hey():
    print('헤이!')
# 실행해보자
hey()


# 변수를 받는 함수 사용
def sum(a,b,c):
    return a+b+c
result=sum(1,2,3)
print(result)


# 조건문
age = 25

if age > 20:
    print('성인입니다.')
else:
    print('청소년입니다.')


# 반복문
ages = [5,10,13,23,25,9]
for a in ages:
    print(a)

# 반복문+조건문
ages = [5,10,13,23,25,9]
for a in ages:
    if a > 20:
        print('성인입니다.')
    else:
        print('청소년입니다.')