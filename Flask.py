from flask import Flask, render_template

# cria um aplicativo web Flask
app = Flask(__name__)

# define uma rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# define uma rota para a página "sobre"
@app.route('/sobre')
def about():
    return render_template('about.html')

# roda o aplicativo web
if __name__ == '__main__':
    app.run(debug=True)