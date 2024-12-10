from django.db import models

class RegistroPesca(models.Model):
<<<<<<< HEAD
    #fecha_jornada =  models.TextField(max_length=50, verbose_name="Día de pesca")
=======
>>>>>>> e4622efc28a26aed0391c0db3ce1f5a4bdd34f5b
    altura_ola = models.FloatField(verbose_name="Altura de la ola (en metros)")
    direccion_ola = models.CharField(max_length=50, verbose_name="Dirección de la ola (cardinal)")
    periodo_ola = models.IntegerField(verbose_name="Periodo de la ola (en segundos)")
    direccion_viento = models.CharField(max_length=50, verbose_name="Dirección del viento (cardinal)")
    velocidad_viento = models.FloatField(verbose_name="Velocidad del viento (en km/h)")
    coeficiente_marea = models.IntegerField(verbose_name="Coeficiente de marea")
    situacion_geografica = models.CharField(max_length=255, verbose_name="Situación geográfica del lugar")
    capturas = models.TextField(verbose_name="Capturas (tipo de especies)")

    creado_el = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pesca en {self.situacion_geografica} - {self.creado_el.strftime('%d/%m/%Y')}"
