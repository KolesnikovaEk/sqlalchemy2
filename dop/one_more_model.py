from flask import Flask
from data import db_session
from data.departments import Departments
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

def main():
    db_session.global_init("db/mars_explorer.db")
    session = db_session.create_session()

    department = Departments()
    department.title = "A"
    department.chief = 5
    department.members = '1, 2'
    department.email = 'a@mail.ru'

    session.add(department)
    session.commit()


if __name__ == '__main__':
    main()