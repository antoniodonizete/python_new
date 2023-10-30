# Generator expression, Iterables e Iterators e, Python

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iterable.__iter__()  # tem __iter__ e __next__ só entrega o próximo valor
print(next(iterator))
print(next(iterator))
print(next(iterator))