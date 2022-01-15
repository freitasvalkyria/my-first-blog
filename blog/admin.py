#

from django.contrib import admin
from .models import Post

#  Para tornar nosso modelo visível na página de administração, é regitrado com "admin.site.register(Post)"
admin.site.register(Post)