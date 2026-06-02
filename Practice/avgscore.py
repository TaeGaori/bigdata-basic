# 함수 정의
def subject():
    """수강 강좌정보를 입력하는 함수"""
    while True:
        title = input('과목명(0:종료) : ')
        if title == '0':
            break
        credit = int(input('학점 수 : '))
        grade = input('취득학점(A,B,C,F) : ')
        course.append([title, credit, grade])

def avg_grade():
    """수강 강좌의 평균평점 확인하는 함수"""
    total = 0
    result = 0
    for i in course:
        if i[2] == 'A':
            total += i[1]
            result += i[1] * 4.5
        elif i[2] == 'B':
            total += i[1]
            result += i[1] * 3.5
        elif i[2] == 'C':
            total += i[1]
            result += i[1] * 2.5
        elif i[2] == 'F':
            total += i[1]
            result += i[1] * 1.5



course = []
while True:
    choice = int(input('1. 수강 강좌정보 입력 2.평균 평점 확인 0.종료 : '))
    if choice < 0 or choice > 3:
        print('없는 번호!')
        continue
    elif choice ==1:
        print('\n< 수강 강좌정보 입력>')
        subject()
        print('< 수강 강좌정보 입력 종료>\n')
    elif choice == 2:
        print('\n< 수강 강좌 목록 >')
        print('과목명\t학점수\t학점')
        print('-' * 20)
        gpa = avg_grade()
        for c in course:
            print(f'{c[0]}\t{c[1]}\t{c[2]}')
        print(f'\n평균평점 : {gpa:}\n')
    elif choice == 0:
        print('초간단 평점평균 계산 시스템 종료')
        break