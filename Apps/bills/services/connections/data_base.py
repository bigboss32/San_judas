from ...models import Gastos
class DataBase():

    def tipo_de_gatsos():
        opciones_tipo_de_gasto = Gastos.TIPOS_DE_GASTO_CHOICES
        return opciones_tipo_de_gasto
