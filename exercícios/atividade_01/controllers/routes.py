from flask import render_template, request, redirect, url_for
import urllib  # envia requisições a url
import json  # faz a conversão de dados json --> dicionario

def init_app(app):
    #array em python
    users = ['Afonso', 'José', 'Isa', 'Yan']
    animelist = [{'Título' : 'Naruto', 'Ano' : 1999, 'Categoria' : 'Ação'}]
    # definindo a rota principal da aplicação '/'
    @app.route('/')
    def home():  # função que será executada ao acessar a rota - view function
        return render_template('index.html') 

    @app.route('/animes', methods=['GET', 'POST'])
    def animes():
        title = 'Bleach'
        year = 2006
        category = 'Ação'
        
        # dicionário em python (objeto)
        brand = {'Nome': 'Dragon Ball Z', 'Estúdio': 'Toei Animation', 'Ano':1989 }
        
        #tratando uma requisição post com request
        if request.method == 'POST':
            #coletando o texto da input
            if request.form.get('user'):
                users.append(request.form.get('user'))
                return redirect(url_for('animes'))
        
        return render_template('animes.html', title=title, year=year, category=category, users=users, brand=brand)

    @app.route('/newanime', methods=['GET', 'POST'])
    def newanime():
        # Tratando a requisição POST
        if request.method == 'POST':
            if request.form.get('title') and request.form.get('year') and request.form.get('category'):
                animelist.append({'Título' : request.form.get('title'), 'Ano' : request.form.get('year'), 'Categoria' : request.form.get('category')})
                return redirect(url_for('newanime'))
        return render_template('newanime.html', animelist=animelist)
    
    @app.route('/apianimes', methods=['GET', 'POST'])
    # criando parametros para rota
    @app.route('/apianimes/<int:id>', methods=['GET', 'POST'])
    def apianimes(id=None):  # parametro opcional
        url = 'https://api.jikan.moe/v4/top/anime'
        response = urllib.request.urlopen(url)
        data = response.read()
        animesList = json.loads(data)
        # verificando se o parametro foi enviado
        if id:
            animeInfo = []
            for anime in animesList:
                if anime['id'] == id:  # comparando os ids
                    animeInfo = anime
                    break
            if animeInfo:
                return render_template('animeinfo.html', animeInfo=animeInfo)
            else:
                return f'anime com a ID {id} não foi encontrado.'
        else:
            return render_template('apianimes.html', animesList=animesList)
