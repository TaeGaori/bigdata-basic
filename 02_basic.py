# 연산자
# 산술 연산자
#  +,  -,  *,  /,  %,  //,  **
#70쪽 동전교환기
#   10000원짜리 지폐를 500원 100원짜리 동전으로 교환

money = 10000
print(money // 500)
print(money // 100)

print()

# 몫, 나머지 --> 구입 가능한 사탕의 수
print(money)
price = 450
numCandy = money // price
change = money % price
print(numCandy)
print(change)

print()

# 대입연산자 = 
# 복합 대입 연산자  +=, -=, *=, /=, %=, **=, //=
a = 10
a += 10 # a = a + 10
print(a)

a -= 5 # a = a - 5
print(a)

a *= 2
print(a)


print()

# 비교연산자
#  >, <, >=(이상), <=(이하), ==(같다), !=(같지 않다)
print(10 == 10)
print(10 > 20)
print(10 != 20)


# 논리 연산자
#   and,  or,  not

a = 10
b = 60
print(a < 50 and b > 50)
print(a < 50 or b < 50)
c = a < 50
print(not c)

print()

# 문자열 연산자
#   + 연결(이어준다)
#   * 반복

print('=' * 50)
head = '파이썬'
tail = '짱!'
print(head + tail)
print('=' * 50)

print()

# in 연산자
print(head in '파이썬 짱 좋아!')
print(tail in '파이썬 짱 좋아!')

print(head not in '파이썬 짱 좋아!')

