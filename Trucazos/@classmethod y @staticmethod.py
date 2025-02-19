class Perro:
    def instance_method(self):
        print(f'llamado desde {self}')

    @classmethod
    def class_method(cls):
        print(f'llamado desde la clase {cls}')

    @staticmethod
    def static_method():
        print('llamado sin instanciar')


luna = Perro()

luna.instance_method() # llamado desde <__main__.Perro object at 0x000001CEAF9A7380>
luna.class_method() # llamado desde la clase <class '__main__.Perro'>
luna.static_method() # llamado sin instanciar


Perro.class_method() # no hay que mandarle la clase, sabe que es él mismo
Perro.instance_method(luna) # le tienes que mandar la instancia
Perro.static_method() # no necesita que se le mande, ni recibe nada