import os
from flask import Flask, render_template, request

def create_app(test_config=None):
    # создаем и настраиваем приложение
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # загружаем конфигурацию экземпляра, если она существует, когда не тестируем
        app.config.from_pyfile('config.py', silent=True)
    else:
        # загружаем конфигурацию теста, если передано
        app.config.from_mapping(test_config)

    # убеждаемся, что папка instance существует
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # простой маршрут, возвращающий "Hello, World!"
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/', methods=['GET', 'POST'])
    def form():
        name = city = hobby = age = None
        if request.method == 'POST':
            name = request.form.get('name')
            city = request.form.get('city')
            hobby = request.form.get('hobby')
            age = request.form.get('age')
        return render_template('form.html', name=name, city=city, hobby=hobby, age=age)

    return app
