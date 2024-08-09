

def authenticate(username, password):
    usernames_bd = ['username1', 'username2'] # вытаскиваем значения
    password_bd = ['password1', 'password2'] # вытаскиваем значения
    if username in usernames_bd:
        if password in password_bd:
            return 'Вход разрешен'
    return 'Вход не разрешен'

