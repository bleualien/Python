from flask import Flask, render_template, request,make_response
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')
    # return "<p>Hello, World!</p>"


@app.route("/products")
def products():
    return "<p>this is product page</p>"

@app.route("/hello__")
def hello_():
    return 'Hello World\n'

@app.route("/hello_")
def response():
    response = make_response()
    response.status_code = 202
    response.headers['content-type']='test/plain'
    return response

@app.route("/hello", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return "<p>you made a request\n</p>"
    elif request.method == 'POST':
        return "You made a POST request\n"
    else:
        return "You will never see this message\n"

# @app.route("/add/<int:number1>/<int:number2>")
@app.route("/add/<number1>/<number2>")
def add(number1, number2):
    return f'{number1} + {number2} = {number1 + number2}'


@app.route("/handle_url_params")
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f'{greeting},{name}'
    else:
        return 'Some Parameters are missing'



if __name__ == "__main__":
    app.run(debug=True, port=8000)
