from django.contrib import admin

# Register your models here.
from .models import PiezaEjecucion
from .models import FaseEjecucion
from .models import MaquinaEjecucion
from .models import Maquinas_Ejecutadas

admin.site.register(PiezaEjecucion)
admin.site.register(FaseEjecucion)
admin.site.register(MaquinaEjecucion)
admin.site.register(Maquinas_Ejecutadas)
