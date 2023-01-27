import rstr

from main.models import Link


def get_random_token():
    while True:
        token = rstr.xeger('^[a-zA-Z0-9]{6}$')
        if not Link.objects.filter(token=token):
            return token
