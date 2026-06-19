from flask import Flask, render_template
from blueprints.member.routes import member_bp
from blueprints.bank.routes import bank_bp


app = Flask(__name__)

app.secret_key = 'test_secret_key'

app.register_blueprint(member_bp)
app.register_blueprint(bank_bp)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/oneline')
def oneline():
    return 'Oneline Diary 페이지'

@app.route('/memo')
def memo():
    return 'Memo 페이지'

@app.route('/todo')
def todo():
    return 'Todo List 페이지'




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')