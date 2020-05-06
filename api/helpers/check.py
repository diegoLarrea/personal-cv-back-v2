from django.contrib.auth.models import User

def check_permissions(user, perm):
    return user.has_perm(perm)