from flask import Flask, render_template

# criando uma instância do flask
app = Flask(__name__, template_folder='views') # __name__ representa o nome da aplicação


# definindo a rota principal da aplicação '/'
@app.route('/')
def home():#função que será executada ao acessar a rota
    return render_template('index.html')

@app.route('/games')
def games():
    return render_template('games.html')


#  se for executado diretamente pelo interpretador
if __name__ == '__main__':
    #iniciando o servidor
    app.run(host='localhost', port=5000, debug=True) 
    