from django.contrib import admin
from .models import *

admin.site.register(Produto)
admin.site.register(Materia_prima)
admin.site.register(Material_do_produto)

