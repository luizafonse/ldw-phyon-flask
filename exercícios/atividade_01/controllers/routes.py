from flask import render_template, request, redirect, url_for


def init_app(app):
    #array em python
    users = ['Afonso', 'José', 'Isa', 'Yan']
    mangalist = [{'Título' : 'Naruto', 'Ano' : 1999, 'Categoria' : 'Ação'}]
    # definindo a rota principal da aplicação '/'
    @app.route('/')
    def home():  # função que será executada ao acessar a rota - view function
        return render_template('index.html') 

    @app.route('/mangas', methods=['GET', 'POST'])
    def mangas():
        title = 'Bleach'
        year = 2006
        category = 'Ação'
        
        # dicionário em python (objeto)
        brand = {'Nome': 'ShounenJump', 'Distribuidora': 'Panini', 'Ano': 2018}
        
        #tratando uma requisição post com request
        if request.method == 'POST':
            #coletando o texto da input
            if request.form.get('user'):
                users.append(request.form.get('user'))
                return redirect(url_for('mangas'))
        
        return render_template('mangas.html', title=title, year=year, category=category, users=users, brand=brand)

    @app.route('/newmanga', methods=['GET', 'POST'])
    def newmanga():
        # Tratando a requisição POST
        if request.method == 'POST':
            if request.form.get('title') and request.form.get('year') and request.form.get('category'):
                mangalist.append({'Título' : request.form.get('title'), 'Ano' : request.form.get('year'), 'Categoria' : request.form.get('category')})
                return redirect(url_for('mangas'))
        return render_template('newmanga.html', mangalist=mangalist)
    