from flask import Flask, render_template

# criando uma instância do flask
# __name__ representa o nome da aplicação
app = Flask(__name__, template_folder='views')


# definindo a rota principal da aplicação '/'
@app.route('/')
def home():  # função que será executada ao acessar a rota
    return render_template('index.html')


@app.route('/games')
def games():
    title = 'Tarisland'
    year = 2022
    category = 'MMORPG'
    players = ['Yan', 'Ferrari', 'Valéria', 'Amanda']
    # dicionário em python (objeto)
    console = {'Nome': 'PlayStation 5', 'Fabricante': 'Sony', 'Ano': 2020}
    return render_template('games.html', title=title, year=year, category=category, players=players, console=console)


#  se for executado diretamente pelo interpretador
if __name__ == '__main__':
    # iniciando o servidor
    app.run(host='localhost', port=5000, debug=True)
