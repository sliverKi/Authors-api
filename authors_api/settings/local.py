from .base import *
from .base import env


SECRET_KEY = env(
    "DJANGO_SECRET_KEY", 
    default='django-insecure-b3!dft229dqxi33is6!0+65p(l0jh9(09*2#=!9yz(s256)y@('
)

DEBUG = True

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1",]