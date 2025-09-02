from flask import render_template, request, redirect, url_for
import urllib  # envia requisições a url
import json  # faz a conversão de dados json --> dicionario


def init_app(app):
    # array em python
    players = ['Yan', 'Ferrari', 'Valéria', 'Amanda']
    gamelist = [{'Título': 'CS 1.6', 'Ano': 2000, 'Categoria': 'FPS Online'}]
    # definindo a rota principal da aplicação '/'

    @app.route('/')
    def home():  # função que será executada ao acessar a rota - view function
        return render_template('index.html')

    @app.route('/games', methods=['GET', 'POST'])
    def games():
        title = 'Tarisland'
        year = 2022
        category = 'MMORPG'

        # dicionário em python (objeto)
        console = {'Nome': 'PlayStation 5', 'Fabricante': 'Sony', 'Ano': 2020}

        # tratando uma requisição post com request
        if request.method == 'POST':
            # coletando o texto da input
            if request.form.get('player'):
                players.append(request.form.get('player'))
                return redirect(url_for('games'))

        return render_template('games.html', title=title, year=year, category=category, players=players, console=console)

    @app.route('/newgame', methods=['GET', 'POST'])
    def newgame():
        # Tratando a requisição POST
        if request.method == 'POST':
            if request.form.get('title') and request.form.get('year') and request.form.get('category'):
                gamelist.append({'Título': request.form.get('title'), 'Ano': request.form.get(
                    'year'), 'Categoria': request.form.get('category')})
                return redirect(url_for('games'))
        return render_template('newGame.html', gamelist=gamelist)

    @app.route('/apigames', methods=['GET', 'POST'])
    # criando parametros para rota
    @app.route('/apigames/<int:id>', methods=['GET', 'POST'])
    def apigames(id=None):  # parametro opcional
        url = 'https://www.freetogame.com/api/games'
        response = urllib.request.urlopen(url)
        data = response.read()
        gamesList = json.loads(data)
        # verificando se o parametro foi enviado
        if id:
            gameInfo = []
            for game in gamesList:
                if game['id'] == id:  # comparando os ids
                    gameInfo = game
                    break
            if gameInfo:
                return render_template('gameinfo.html', gameInfo=gameInfo)
            else:
                return f'Game com a ID {id} não foi encontrado.'
        else:
            return render_template('apigames.html', gamesList=gamesList)
