members = []

while True:
    print('1. 회원가입')
    print('2. 로그인')
    print('3. 특정 회원정보')
    print('4. 모든 회원정보')
    print('99.종료')

    menu = int(input('선택: '))

    if menu == 1:
        memberId = (input('아이디 입력: '))
        memberPw = (input('비밀번호 입력: '))
        memberEm = (input('이메일아이디 입력: '))
        memberNum = (input('연락처 입력: '))
        
        member = {
            'id': memberId,
            'pw': memberPw,
            'email': memberEm,
            'phoneNum': memberNum
        }
        members.append(member)
        print(f'회원가입완료')

    elif menu == 2:
        loginId = input('ID입력: ')
        loginPw = input('PW입력: ')

    loginSuccess = False

    for member in members:
        loginSuccess = True
        break
    
    if loginSuccess:
        print('로그인 성공')
    else:
        print('로그인 실패')
        