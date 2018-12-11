from django.contrib import admin

# Register your models here.
from .models import Pieza
from .models import Fase
from .models import Maquina
from .models import Maquinas_Ejecutadas

admin.site.register(Pieza)
admin.site.register(Fase)
admin.site.register(Maquina)
admin.site.register(Maquinas_Ejecutadas)
