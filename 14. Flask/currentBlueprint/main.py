from flask import Flask
from blueprint.helloworld.helloworld import helloworld_bp
from blueprint.calculator.calculator import calculateor_bp

app = Flask(__name__)
app.register_blueprint(helloworld_bp)
app.register_blueprint(calculateor_bp, url_prefix="/calculator")

if __name__=='__main__':
    app.run(debug=True)
