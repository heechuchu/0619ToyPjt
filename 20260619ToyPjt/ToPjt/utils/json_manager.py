import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FILE = os.path.join(BASE_DIR, 'db', 'member.json')
ACCOUNT_FILE = os.path.join(BASE_DIR, 'db', 'account.json')

def load_members():
    try:
        with open(FILE, encoding='utf-8') as f:
            return json.load(f)
        
    except:
        return {}
    

def save_members(members):
    with open(FILE, 'w', encoding='utf-8') as f:
        json.dump(
            members,
            f,
            ensure_ascii= False,
            indent=4
            
        )

def load_accounts():

    try:
        with open(ACCOUNT_FILE, encoding='utf-8') as f:
            return json.load(f)
        
    except:
        return {}
    
def save_accounts(accounts):
    with open(ACCOUNT_FILE, 'w', encoding='utf-8') as f:
        json.dump(
            accounts,
            f,
            ensure_ascii= False,
            indent=4
            
        )    