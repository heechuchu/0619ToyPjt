from flask import Blueprint, render_template, request , session, redirect
from utils.json_manager import load_members, save_members


member_bp = Blueprint(
    'member',
    __name__,
    url_prefix='/member'
)
# signup form
@member_bp.route('/signup_form', methods=['GET'])
def signup_form():
    return render_template('signup_form.html')

# signup_confirm
@member_bp.route('/signup_confirm', methods=['POST'])
def signup_confirm():
    mId = request.form['mId']
    mPw = request.form['mPw']
    mMail = request.form['mMail']
    mPhone = request.form['mPhone']

    members = load_members()


    # id 중복체크 
    if mId in members:
        return render_template('signup_result.html',
                               result='NG')

    members[mId] = {
        "mId": mId,
        "mPw": mPw,
        "mMail": mMail,
        "mPhone": mPhone,
    }

    save_members(members)

        
    return render_template('signup_result.html',
                               result='OK')

# signin_form

@member_bp.route('/signin_form', methods=['GET'])
def signin_form():

    result = request.args.get('result')

    return render_template('signin_form.html', result = result)

# signin_confirm
@member_bp.route('/signin_confirm', methods=['POST'])
def signin_confirm():
    mId = request.form['mId']
    mPw = request.form['mPw']

    members = load_members()

    if mId in members and members[mId]['mPw'] == mPw:
        session['signinedMemberId'] = mId
        return render_template('signin_result.html')
    
    return redirect('/member/signin_form?result=fail')


# signout_confirm

@member_bp.route('/signout_confirm', methods=['GET'])
def signout_confirm():

    # session.clear()
    session.pop('signinedMemberId', None)

    return redirect('/')

# member/modify_form
@member_bp.route('/modify_form')
def modify_form():
    members = load_members()
    member = members[session.get('signinedMemberId')]  # 현재로그인되있는회원정보수집

    return render_template(
        'modify_form.html',
        member = member
    )

# member/modify_confirm
@member_bp.route('/modify_confirm', methods=['POST'])
def modify_confirm():

    '''
    현재 로그인 되어있는 회원 ID가 gildong 라면
    '''
    mId = request.form['mId']
    mPw = request.form['mPw']
    mMail = request.form['mMail']
    mPhone = request.form['mPhone']

    members = load_members()
    member = members[mId]
    member['mPw'] = mPw
    member['mMail'] = mMail
    member['mPhone'] = mPhone

    save_members(members)

    return render_template('modify_result.html')

# delete_confirm
@member_bp.route('/delete_confirm')
def delete_confirm():

    members = load_members()
    signinedMemberId = session.get('signinedMemberId')
    del members[signinedMemberId]
    save_members(members)

    session.clear()

    return render_template('delete_result.html')