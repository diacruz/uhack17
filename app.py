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
    # item  = list(['item', 'item2'])   
    form = Search(request.form)     
    if request.method == 'POST':
        userInput = form.language.data      
        if userInput == 'Python':
            beginner_response = list(['working', 'working2'])
            intermideate_response = list(['working'])
            expert_response = list(['working'])      
        if userInput == 'Java':
            beginner_response = list(['working'])
            intermideate_response = list(['working'])
            expert_response = list(['working'])
        if userInput == 'C#':
            beginner_response = list(['working'])
            intermideate_response = list(['working'])
            expert_response = list(['working'])
        if userInput == 'Ruby':
            beginner_response = list(['working'])
            intermideate_response = list(['working'])
            expert_response = list(['working'])
        if userInput == 'Swift':
            beginner_response = list(['working'])
            intermideate_response = list(['working'])
            expert_response = list(['working'])
              
        return render_template('response.html', beginner_response = beginner_response, intermideate_response = intermideate_response, expert_response = expert_response )
    return render_template('response.html')

class Search(FlaskForm):
    language = StringField('Language')

if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'this is suppose to be secret'
    app.run(host="0.0.0.0", port=3000, debug=True)

    