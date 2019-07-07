from getpass import getpass
import sys

from webapp import create_app
from webapp.database import db
from webapp.user.models import User

app = create_app()

with app.app_context():
    username = input('Введите логин: ')
    first_name = input('Введите имя:')
    last_name = input('Введите фамилию:')

    if User.query.filter(User.username == username).count():
        print('Такой пользователь уже существует')
        sys.exit(0)

    password1 = getpass(prompt='Введите пароль: ')
    password2 = getpass(prompt='Повторите пароль: ')
    if password1 != password2:
        print('Пароли не совпадают')
        sys.exit(0)

    new_user = User(username=username, first_name=first_name, last_name=last_name, password=password1, privilege=True, need_reset=False)
    db.session.add(new_user)
    db.session.commit()
    print('Создан пользователь с id={}'.format(new_user.username))
