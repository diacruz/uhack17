from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length
from wtforms import Form, StringField


app = Flask(__name__)

@app.route("/")
def home():
    form = Search(request.form)
    return render_template('main.html', form = form)

@app.route("/response", methods = ['POST'])
def response():
    # 1)get response from form
    # 2)create if comparing what the from was passed
    # 3)return something from that if statement

    # Ex: 
    # if request.form == 'Python':
    #     beginner_reponse = ['idea 1', 'idea 2']
    #     intermideate_reponse = ['idea2']
    #     expert_reponse = ['idea2']
    # if request.form == 'Java':
    #     beginner_reponse = ['idea 1', 'idea 2']
    #     intermideate_reponse = ['idea2']
    #     expert_reponse = ['idea2']
    # return render_template('response.html' beginner_response = beginner_response ...)
    return render_template('response.html')

class Search(FlaskForm):
    language = StringField('Language')

if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'this is suppose to be secret'
    app.run(host="0.0.0.0", port=3000, debug=True)

    