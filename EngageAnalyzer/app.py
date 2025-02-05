import ea
from flask import Flask, render_template, request
app = Flask(__name__)

# Home route with form to input text
options_name = ["옐언니", 
                "새옴"]
options_query = ["의 가장 찐팬 5명을 알려줘", 
                 "의 가장 좋아하는 선물은 무엇이야", 
                 "의 가장 좋아하는 음식은 무엇이야"]

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    user_query = ""
    output = ""
    if request.method == 'POST':
        user_name = request.form.get("select_name")
        user_query = request.form.get('select_query')
        names, reasons = ea.get_response(user_name, user_query)
        for name, reason in zip(names, reasons):
            output+=f"{name}, {reason}"
            output+="\n"
        result = f"{output}" if output else "No input provided"
        user_query = f"{user_query}" if user_query else "No input provided"

    return render_template('index.html', 
                           options_name = options_name,
                           options_query = options_query,
                           result=result,
                           user_query=user_query)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)