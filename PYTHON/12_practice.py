# PT - 1

# univ = input('학교 :')
# dept = input('학과 :')
# name = input('이름 :')
# phone = input('연락처 :')

# print('{} 학생은 {}학교 {}에 재학 중이며, 연락처는 {}입니다.'.format(name, univ, dept, phone))
# print(f'{name} 학생은 {univ}에 {dept}에 재학 중이며, 연락처는 {phone}입니다.')


#------------------------------------------------------------------------------------------------
# PT - 2

# name = input('이름 입력 : ')
# age = input('출생년도 입력 : ')

# print('2023년 시점, {}의 한국 나이는 {}살입니다.'.format(name, int(2023+1-float(age))))

#------------------------------------------------------------------------------------------------
# PT - 3
# month = int(input('월 입력 : '))
# if 3 <= month <= 5:
#     print(f'{month}월은 봄')
# elif 6 <= month <= 8:
#     print(f'{month}월은 여름')
# elif 9 <= month <= 11:
#     print(f'{month}월은 가을')
# else:
#     print(f'{month}월은 겨울')

#------------------------------------------------------------------------------------------------
# PT - 4
# a = int(input('1차 점수 입력 : '))
# b = int(input('2차 점수 입력 : '))
# avg = (a + b) / 2 

# if a >= 50 and b >= 50 and avg >=50 :
#     print('합격')
# else:
#     print('불합격')

#------------------------------------------------------------------------------------------------
# PT - 5
# 라이브러리 불러오기
# import 불러올 라이브러리명
# 그 안의 함수 호출(실행)
# 라이브러리명.함수명()
# import random

# com = random.randint(1, 30) # 1~30 중 하나의 정수 추철
# print('<<1~30 숫자 맞히기 게임>>')
# while True:
#     player = int(input('숫자 입력(종료는 0) : '))
#     if player == 0:
#         break
#     elif player == com:
#         print('정답!!')
#         break
#     elif player > com:
#         print('더 작은 숫자 입력!')
#     else :
#         print('더 큰 숫자를 입력!')
    
#------------------------------------------------------------------------------------------------
# PT - 6
# import random

# lotto = []  # 빈 리스트
# while True:
#     num = random.randint(1, 45) #1~45 정수 중에서 하나 추출
#     if num not in lotto: #중복이 안되었다!
#         lotto.append(num)
#     if len(lotto) == 6: # len(리스트 또는 문자열) --> 총 개수(총 글자수)
#         break

# print('<< 생성된 로또 번호 >>')
# print(lotto)
# for i in range(6):
#     print(f'{lotto[i]}', end = ' ')

# #ramdom.sample(범위, 개수) --> 범위에서 개수만큼 중복되지 않는 수를 추출
# lotto2 = random.sample(range(1, 46), 6)
# print(lotto2)

#------------------------------------------------------------------------------------------------

# PT - 7
# import random
# word = ["무지개", "도서관", "자전거", "여름밤", "고양이", "해바라기", "파도", "구름", "초콜릿", "별자리"]
# input('타자게임 시작 (엔터 입력)')

# w = random.choice(word)
# n = 1 # 문제번호
# while True:
#     print(f'문제{n} (종료 0) : {w}')
#     my = input()
#     if my == '0': # 0을 입력하면 종료!
#         break
#     elif my == w:
#         print('맞음!!')
#         w = random.choice(word)
#     else:
#         print('틀림! 다시!')
#     n += 1 #문제 번호 증가



# 7
# import random

# word = ['낙하','불구덩이','몰라'] # 워드 모음
# c = 1
# q = random.choice(word) # 첫번째 워드 초기화
# while True: # 문제 반복 시작
    
#     ans = input(f"문제 {c} (종료: 0) : {q}\n")
#     if ans == '0':
#         break
#     if q == ans:
#         print('정답')
#         q = random.choice(word) # 다음 문제 갱신
#         c += 1 # 다음 문제 번호 갱신
#     else:
#         print("틀림")


#------------------------------------------------------------------------------------------------
# PT - 8
# vote = {'대성리':0 , '춘천':0 , '을왕리':0, '청평':0}

# for key in vote:
#     print(f'{key} : {vote[key]}표' , end =' ')
# print('\n')
# print('<< MT 장소 투표 >>')
# while True:
#     area = input('장소 : ')
#     if not area:
#         break
#     vote[area] = vote[area] +1

# for key in vote:
#     print(f'{key} : {vote[key]}표' , end =' ')
# print('\n')

# # max(값들) : 최대값
# # min(값들) : 최소값
# max_key = max(vote, key = vote.get)
# print(f'최다득표 : {max_key} {vote[max_key]}표')

#------------------------------------------------------------------------------------------------
# PT - 10
# def price(menue):
#     if menue == 1:
#         # print('아메리카노: 3000원')
#         m = '아메리카노'
#         p = 3000
#     elif menue == 2:
#         # print('카페라떼: 4000원')
#         m = '카페라떼'
#         p = 4000
#     elif menue == 3:
#         # print('바닐라라떼: 4500원')
#         m = '바닐라라떼'
#         p = 4500
#     else:
#         print('실수')
#     print(f'{m}: {p:,}원')  #천단위 구분 기호 추가

# menue = int(input('메뉴선택(1:아메리카노/2:카페라떼/3.바닐라라데)'))
# price(menue)

#------------------------------------------------------------------------------------------------
# PT - 11
# files = ['report.hwp', 'newJeans', 'Attention.png', 'ditto.jpg','address.xslx']

# result = filter(lambda x: 'jpg' in x or 'png' in x, files)
# print(list(result))