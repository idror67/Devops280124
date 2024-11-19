from flask import Flask, render_template

app = Flask(__name__)

my_listfromdb = ["sunday", "tuesday", "wednesday", "friday"]

# here we can define different routes

@app.route("/")
def index():
    print("got the request!")


@app.route("/start")
def start():
    return "<h1>hello from flask</h1>"


@app.route('/html')
def html():
    return "<h1>Hello world!</h1>  <ul><li>sunday</li><li>wendesday</li> </ul>"


@app.route('/table')
def table():
    return render_template("index.html")


@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/welcome/arja')
def welcome_arja():
    return render_template("welcome.html", first_name = "arja" , listfromdb = my_listfromdb)

@app.route('/welcome/john', methods=['POST'])
def welcome_john():
    return render_template("welcome.html", first_name = "john" , last_name = "snow")


if __name__ == "__main__":
    app.run(port=5000, debug=True ) 

