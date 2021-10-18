from django.urls import path
from django.conf.urls import url
from sistema.views import *
urlpatterns = [
    path('', index),
    url(r'^nuevoelectro', electro_view, name='nuevoelectro'),
    url(r'^listelectro', electro_list, name='listelectro'),
    url(r'^editelectro/(?P<id_electro>\d+)', electro_edit, name='editelectro'),
    url(r'^deleteelectro/(?P<id_electro>\d+)', electro_delete, name='deleteelectro'),
    url(r'^nuevaluz', luz_view, name='nuevaluz'),
    url(r'^listluz', luz_list, name='listluz'),
    url(r'^editluz/(?P<id_electro>\d+)', luz_edit, name='editluz'),
    url(r'^deleteluz/(?P<id_electro>\d+)', luz_delete, name='deleteluz'),
    url(r'^nuevoclimatizador', climatizador_view, name='nuevoclimatizador'),
    url(r'^listclima', clima_list, name='listclima'),
    url(r'^editclima/(?P<id_electro>\d+)', clima_edit, name='editclima'),
    url(r'^deleteclima/(?P<id_electro>\d+)', clima_delete, name='deleteclima'),
    url(r'^grafico', grafico, name='grafico'),
    url(r'^nuevahora', horario_view, name='nuevahora'),
    url(r'^listhora', horario_list, name='listhora'),
    url(r'^deletehora/(?P<id_horario>\d+)', horario_delete, name='deletehora'),
]
