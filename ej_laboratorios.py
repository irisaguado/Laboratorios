class Producto():
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

class Medicamento(Producto):
    def __init__(self,nombre, cantidad, precio, nom_componente, porcentaje):
        super().__init__(nombre, cantidad, precio)
        self.nom_componente = nom_componente
        self.porcentaje = porcentaje

    def get_nom_componente(self):
        return self.nom_componente

    def get_porcentaje(self):
        return self.porcentaje

class Laboratorio():
    def __init__(self, nombre, list_productos):
            self.nombre = nombre
            self.list_productos = list_productos

    def get_productos(self):
        nom_productos = []
        for i in range(len(self.list_productos)):
            producto = self.list_productos[i].get_nombre()
            nom_productos.append(producto)
        return nom_productos

laboratorioA = []
laboratorioB = []

jarabe = Medicamento('jarabe', 7, 20, 'glucosa', 0.5)
laboratorioA.append(jarabe)
laboratorioB.append(jarabe)
print('El', jarabe.nombre, 'contiene', jarabe.get_nom_componente(), 'en un', jarabe.get_porcentaje(), '%.')

paracetamol = Medicamento('paracetamol', 8, 3, 'acido', 0.9)
laboratorioA.append(paracetamol)
print('El precio del', paracetamol.nombre, 'es', paracetamol.get_precio())

cremas = Producto('cremas', 15, 2)
laboratorioB.append(cremas)
print('La cantidad de', cremas.nombre, 'es', cremas.get_cantidad())

labA = Laboratorio('labA', laboratorioA)
print('El', labA.nombre, 'tiene', labA.get_productos())
labB = Laboratorio('labB', laboratorioB)
print('El', labB.nombre, 'tiene', labB.get_productos())
