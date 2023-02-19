from django.contrib.auth import get_user_model


def reset_password(u, password):

    try:
        user = get_user_model().objects.get(email=u)
    except:
        return "User could not be found"

    user.set_password(password)
    user.save()
    return "Password has been changed successfully"


user_n = 'paynedestinne@gmail.com'
passWord = 'DesMUGE123'


def password_reset():
    the_reset_button = reset_password(user_n, passWord)

    while the_reset_button:
        print(the_reset_button)
        break


password_reset()
