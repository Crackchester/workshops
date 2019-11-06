from flask_login import login_user
from demo import login, mysql

def login_user_with_form(form):
    # Check form
    if not form.validate():
        return False

    # Hurr durr very important security checks
    security = Security(form)
    if not security.super_strong_bruteforce_check():
        return False

    if not security.very_cool_device_finger_printing():
        return False

    if not security.hundredth_check():
        return False

    # Get user from database
    query = ("SELECT username FROM Users WHERE username = '{name}' AND password = '{passwd}'"
                .format(name=form.username.data, passwd=form.password.data))
    print(query)
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    (user,) = cursor.fetchall()[0]
    return login_user(User(user)) 

class User(object):
    def __init__(self, username):
        self.username = username

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

    def is_active(self):
        return True


class Security(object):
    def __init__(self, user):
        self.user = user

    def super_strong_bruteforce_check(self):
        return True

    def very_cool_device_finger_printing(self):
        return True

    def hundredth_check(self):
        return True

@login.user_loader
def load_user(id):
    return User(id)

def search_user(form):
    query = ("SELECT * FROM Users WHERE username like '{name}' AND cool = '{cool}'"
                    .format(name=form.username.data, cool=form.cool.data))

    print(query)
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    user = cursor.fetchall()
    return user;