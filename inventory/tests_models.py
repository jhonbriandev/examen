from django.test import TestCase
from .models import Product
# importar pytest
# importar decorador

class ErrorinProduct():
    pass
#decorador para feature
# crear tabla temporal con datos temporales

class TestProduct:

    def test_max_length_description(self):
        if len(self.descprition) > 200:
            raise ErrorinProduct ('Texto demasiado largo')
        return self.description
    def test_name_value_blank(self):
        if self.name == '':
            raise ErrorinProduct ('No puede dejar esta campo vacio')
        return self.name
    def test_stock_not_positive(self):
        if self.stock < 1:
            raise ErrorinProduct ('El stock no puede ser negativo')
        return self.stock 