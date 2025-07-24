from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/")
def about():
    return render_template("about.html")

@app.route("/pets")
def pets():
    return render_template("pets.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/buscar")
def buscar():
    return render_template("buscar.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/registracion")
def registracion():
    return render_template("registracion.html")

if __name__ == "__main__":
    app.run(debug=True)
