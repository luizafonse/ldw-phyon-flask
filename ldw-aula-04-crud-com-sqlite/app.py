from flask import Flask, render_template
# IMPORTANDO O CONTROLLER (routes.py)
from controllers import routes
#importando os models 
from models.database import db
#importando biblioteca para manipulação do S.O(dir e etc)
import os

# criando uma instância do flask
# __name__ representa o nome da aplicação
app = Flask(__name__, template_folder='views')

routes.init_app(app)

#extraindo o diretorio absoluto do arquivo
dir = os.path.abspath(os.path.dirname(__file__))

#criando o arquivo no banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dir, 'models/game.sqlite3')

#  se for executado diretamente pelo interpretador
if __name__ == '__main__':
    #enviando o flask para o sqlalchemy
    db.init_app(app=app)
    #verificar no inicio da aplicação se o banco ja existe. Se não ele cria.
    with app.test_request_context():
        db.create_all()
        
    # iniciando o servidor
    app.run(host='0.0.0.0', port=5000, debug=True)
