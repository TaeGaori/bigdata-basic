# #회원이면 ' 어서오세요'라는 인사말 출력
# member = input('회원입니까?? (y/n)')
# if member == 'y':
#     print('반갑습니다!')
# else:
#     print('회원가입하세요!')


#-------------------------------------
# member = input('회원입니까?? (y/n)')
# if member == 'y':
#     print('반갑습니다!')
# elif member == 'n':
#     print('회원가입하세요!')
# else:
#     print('y와 n중에 입력하세요!')


age = int(input('나이를 입력하세요 : '))
price = 20000
if age < 6:
    print('무료')
elif age < 60 :
    print(f'{price}원')
else:
    print(f'{int(price * 0.5 )} 원')

