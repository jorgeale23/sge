import datetime
import intervals as I
from sistema.models import *
class DiasdeMes:
 def es_bisiesto(self,anio: int):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)
 def obtener_dias_del_mes( self, mes: int, anio: int):
    # Abril, junio, septiembre y noviembre tienen 30
    DiasdeMes.es_bisiesto(self, anio)
    if mes in [4, 6, 9, 11]:
        return 30
    # Febrero depende de si es o no bisiesto
    if mes == 2:
        if self.es_bisiesto(anio):
            return 29
        else:
            return 28
    else:
        # En caso contrario, tiene 31 días
        return 31

 def contar_dias( self, mes: int, anio: int):
    dias = range(1,self.obtener_dias_del_mes(self, mes, anio))
    lunes = 0
    martes = 0
    miercoles = 0
    jueves = 0
    viernes = 0
    sabado = 0
    domingo = 0
    for i in dias:
       if datetime.datetime(anio, mes, i).isoweekday() == 1:
          lunes += 1
       if datetime.datetime(anio, mes, i).isoweekday() == 2:
          martes += 1
       if datetime.datetime(anio, mes, i).isoweekday() == 3:
          miercoles += 1
       if datetime.datetime(anio, mes, i).isoweekday() == 4:
          jueves += 1
       if datetime.datetime(anio, mes, i).isoweekday() == 5:
          viernes += 1
       if datetime.datetime(anio, mes, i).isoweekday() == 6:
          sabado += 1
       if datetime.datetime(anio, mes, i).isoweekday() == 7:
          domingo += 1
    return [lunes, martes, miercoles, jueves, viernes, sabado, domingo]

class HorasActivas:
   def interseccion(self,i11, i12, i21, i22):
       return(I.closed(i11,i12) & I.closed(i21,i22))

   def totalhorasluz(self,mes, anio):
       horatotal = 0
       horalunes = HoraCasa.objects.filter(Dia=1)
       horamartes = HoraCasa.objects.filter(Dia=2)
       horamiercoles = HoraCasa.objects.filter(Dia=3)
       horajueves = HoraCasa.objects.filter(Dia=4)
       horaviernes = HoraCasa.objects.filter(Dia=5)
       horasabado = HoraCasa.objects.filter(Dia=6)
       horadomingo = HoraCasa.objects.filter(Dia=7)
       dm = DiasdeMes
       d = dm.contar_dias(dm, mes, anio)

       horaluz = HoraLuz.objects.get(Mes=str(datetime.datetime.now().month))
       h = HorasActivas()
       for dia in horalunes:
           haux = h.interseccion(horaluz.PuestaSol,
                                      datetime.datetime.strptime('23:59:59', '%H:%M:%S').time(),
                                      dia.Inicio,
                                      dia.Fin)
           if not haux.is_empty():
                horatotal= horatotal + (((haux.upper.hour * 60) + haux.upper.minute) - (
                        (haux.lower.hour * 60) + haux.lower.minute)) * d[0]

           haux = h.interseccion(datetime.datetime.strptime('00:00:00', '%H:%M:%S').time(),
                                 horaluz.Amanecer,
                                 dia.Inicio,
                                 dia.Fin)
           if not haux.is_empty():
               horatotal = horatotal + (((haux.upper.hour * 60) + haux.upper.minute) - (
                           (haux.lower.hour * 60) + haux.lower.minute)) * d[0]


       for dia in horamartes:
           haux = h.interseccion(horaluz.PuestaSol,
                                      datetime.datetime.strptime('23:59:59', '%H:%M:%S').time(),
                                      dia.Inicio,
                                      dia.Fin)
           if not haux.is_empty():
                horatotal= horatotal + (((haux.upper.hour * 60) + haux.upper.minute) - (
                        (haux.lower.hour * 60) + haux.lower.minute)) * d[1]

           haux = h.interseccion(datetime.datetime.strptime('00:00:00', '%H:%M:%S').time(),
                                 horaluz.Amanecer,
                                 dia.Inicio,
                                 dia.Fin)
           if not haux.is_empty():
               horatotal = horatotal + (((haux.upper.hour * 60) + haux.upper.minute) - (
                           (haux.lower.hour * 60) + haux.lower.minute)) * d[1]


       for dia in horamiercoles:
           haux = h.interseccion(horaluz.PuestaSol,
                                      datetime.datetime.strptime('23:59:59', '%H:%M:%S').time(),
                                      dia.Inicio,
                                      dia.Fin)
           if not haux.is_empty():
                horatotal= horatotal + (((haux.upper.hour * 60) + haux.upper.minute) - (
                        (haux.lower.hour * 60) + haux.lower.minute)) * d[2]

           haux = h.interseccion(datetime.datetime.strptime('00:00:00', '%H:%M:%S').time(),
                                 horaluz.Amanecer,
                                 dia.Inicio,
                                 dia.Fin)
           if not haux.is_empty():
               horatotal = horatotal + (((haux.upper.hour * 60) + haux.upper.minute) - (
                           (haux.lower.hour * 60) + haux.lower.minute)) * d[2]

       for dia in horajueves:
           haux = h.interseccion(horaluz.PuestaSol,
                                      datetime.datetime.strptime('23:59:59', '%H:%M:%S').time(),
                                      dia.Inicio,
                                      dia.Fin)
           if not haux.is_empty():
                horatotal= horatotal + (((haux.upper.hour * 60) + haux.upper.minute) - (
                        (haux.lower.hour * 60) + haux.lower.minute)) * d[3]

           haux = h.interseccion(datetime.datetime.strptime('00:00:00', '%H:%M:%S').time(),
                                 horaluz.Amanecer,
                                 dia.Inicio,
                                 dia.Fin)
           if not haux.is_empty():
               horatotal = horatotal + (((haux.upper.hour * 60) + haux.upper.minute) - (
                           (haux.lower.hour * 60) + haux.lower.minute)) * d[3]

       for dia in horaviernes:
           haux = h.interseccion(horaluz.PuestaSol,
                                      datetime.datetime.strptime('23:59:59', '%H:%M:%S').time(),
                                      dia.Inicio,
                                      dia.Fin)
           if not haux.is_empty():
                horatotal= horatotal + (((haux.upper.hour * 60) + haux.upper.minute) - (
                        (haux.lower.hour * 60) + haux.lower.minute)) * d[4]

           haux = h.interseccion(datetime.datetime.strptime('00:00:00', '%H:%M:%S').time(),
                                 horaluz.Amanecer,
                                 dia.Inicio,
                                 dia.Fin)
           if not haux.is_empty():
               horatotal = horatotal + (((haux.upper.hour * 60) + haux.upper.minute) - (
                           (haux.lower.hour * 60) + haux.lower.minute)) * d[4]


       for dia in horasabado:
           haux = h.interseccion(horaluz.PuestaSol,
                                      datetime.datetime.strptime('23:59:59', '%H:%M:%S').time(),
                                      dia.Inicio,
                                      dia.Fin)
           if not haux.is_empty():
                horatotal= horatotal + (((haux.upper.hour * 60) + haux.upper.minute) - (
                        (haux.lower.hour * 60) + haux.lower.minute)) * d[5]

           haux = h.interseccion(datetime.datetime.strptime('00:00:00', '%H:%M:%S').time(),
                                 horaluz.Amanecer,
                                 dia.Inicio,
                                 dia.Fin)
           if not haux.is_empty():
               horatotal = horatotal + (((haux.upper.hour * 60) + haux.upper.minute) - (
                           (haux.lower.hour * 60) + haux.lower.minute)) * d[5]

       for dia in horadomingo:
           haux = h.interseccion(horaluz.PuestaSol,
                                      datetime.datetime.strptime('23:59:59', '%H:%M:%S').time(),
                                      dia.Inicio,
                                      dia.Fin)
           if not haux.is_empty():
                horatotal= horatotal + (((haux.upper.hour * 60) + haux.upper.minute) - (
                        (haux.lower.hour * 60) + haux.lower.minute)) * d[6]

           haux = h.interseccion(datetime.datetime.strptime('00:00:00', '%H:%M:%S').time(),
                                 horaluz.Amanecer,
                                 dia.Inicio,
                                 dia.Fin)
           if not haux.is_empty():
               horatotal = horatotal + (((haux.upper.hour * 60) + haux.upper.minute) - (
                           (haux.lower.hour * 60) + haux.lower.minute)) * d[6]

       return (horatotal/60)

#ob = Solution()
#intervals = [[datetime.datetime.strptime('12:10', '%H:%M'), datetime.datetime.strptime('12:45', '%H:%M')],[datetime.datetime.strptime('12:10', '%H:%M'), datetime.datetime.strptime('12:21', '%H:%M')]]
#print(ob.solve(intervals))