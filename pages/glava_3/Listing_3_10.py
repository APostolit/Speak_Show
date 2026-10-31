# Листинг 3.10
from decimal import Decimal
a = 0.1
print ('Дано число a=', a)
b = a + a + a
print('Итог с точностью по умолчанию b=', b)

a = Decimal('0.1')
b = a + a + a
print('Итог с заданной точностью b=', b)