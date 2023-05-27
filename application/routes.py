from application import app
from flask import render_template, request
from application.forms import SignUpForm, SignInForm

@app.route("/")
@app.route("/index")
@app.route("/hoho")
def index():
    return render_template("index.html", index=True, login=False)

@app.route("/products")
@app.route("/items")
def products():
    dataProducts = [["1", "Dell", "1200.00"], ["2","HP","1100.00"], ["3","Mac","1500.00"], ["4","Acer","1000.00"]]
    print(dataProducts[0][1])
    return render_template("products.html", products=True, dataProducts=dataProducts)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    username = request.form.get("username", "")
    email = request.form.get("email", "")
    password = request.form.get("password", "")
    data = {"username": username, "email": email, "password": password}
    form = SignUpForm();
    return render_template("signup.html", signup = True, data = data, form=form)

@app.route("/basket")
def basket():
    return render_template("basket.html", basket = True, login = False)

@app.route("/signin")
def signin():
    username = request.form.get("usrname", "")
    password = request.form.get("password", "")
    data = {"username": username, "password": password}
    form = SignInForm();
    return render_template("signin.html", signin = True, data = data, form = form, login = True)
