from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods = ['POST'])
def info():
    print('Got POST Info')
    print(request.form)
    name_form = request.form['name']
    lang_form = request.form['language']
    return render_template('submit.html', name_temp = name_form, lang_temp = lang_form,)


if __name__=="__main__":
    app.run(debug=True)