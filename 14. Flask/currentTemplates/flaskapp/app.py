from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    # myvalue = 'Saina'
    # myresult = 10 + 42
    mylist = [10,20,30]
    return render_template('index.html',mylist=mylist) 
# myvalue=myvalue, myresult=myresult, 

@app.route('/other')
def other():
    some_text = 'Hello World'
    return render_template('other.html', some_text=some_text) 

@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('other'))

@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@app.template_filter('repeat')
def repeat(s, times=2):
    return s * times

@app.template_filter('alternate_case')
def alternate_case(s):
    return ''.join([c.upper()if i % 2 == 0 else c.lower() for i, c in enumerate(s)])
    
    

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)