from flask import Blueprint, render_template, session, redirect, request
from utils.json_manager import load_accounts
from utils.json_manager import save_accounts

bank_bp = Blueprint(
    'bank',
    __name__,
    url_prefix='/bank'
)

@bank_bp.route('/')
def bank_home():
    if not session.get('signinedMemberId'):
        return redirect('/member/signin_form')
    
    return render_template('bank/bank_home.html')

# 계좌생성
@bank_bp.route('/create_form')
def create_form():
    return render_template('bank/create_form.html')

@bank_bp.route('/create_confirm', methods=['POST'])
def create_confirm():

    signinedMemberId = session.get('signinedMemberId')

    accounts = load_accounts()

    account_no = f'100-{len(accounts)+ 1:06d}'
    
    accounts[account_no] = {
        'accountNo': account_no,
        'owner': signinedMemberId,
        'balance': 0
    }

    save_accounts(accounts)
    return redirect('/bank/list_form')


# 계좌 조회

@bank_bp.route('/list_form')
def account_list():

    signinedMemberId = session.get('signinedMemberId')

    accounts = load_accounts()
    my_accounts = []

    for account in accounts.values():

        if account.get('owner') == signinedMemberId:
            my_accounts.append(account)

    return render_template(
        'bank/list_form.html',
        account = my_accounts
    )

# 입금
@bank_bp.route('/deposit_form')
def deposit_form():

    signinedMemberId = session.get('signinedMemberId')

    accounts = load_accounts()
    my_accounts = []

    for account in accounts.values():
        if account.get('owner') == signinedMemberId:
            my_accounts.append(account)

        return render_template(
            'bank/deposit_form.html',
            accounts = my_accounts
        )
    



@bank_bp.route('/deposit_confirm', methods=['POST'])
def deposit_confirm():
    
    account_no = request.form['accountNo']
    amount = int(request.form['amount'])

    accounts = load_accounts()

    accounts[account_no]['balance'] += amount

    save_accounts(accounts)
    return redirect('/bank/list/form')


# 출금
