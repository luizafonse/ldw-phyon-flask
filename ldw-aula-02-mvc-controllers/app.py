from flask import Flask, render_template
# IMPORTANDO O CONTROLLER (routes.py)
from controllers import routes

# criando uma instância do flask
# __name__ representa o nome da aplicação
app = Flask(__name__, template_folder='views')

routes.init_app(app)

#  se for executado diretamente pelo interpretador
if __name__ == '__main__':
    # iniciando o servidor
    app.run(host='localhost', port=5000, debug=True)
