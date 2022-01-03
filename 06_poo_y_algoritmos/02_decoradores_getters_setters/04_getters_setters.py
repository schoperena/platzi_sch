class Millas:
	def __init__(self):
		self.__distancia = 0

	# Función para obtener el valor de _distancia
	# Usando el decorador property
	@property
	def obtener_distancia(self):
		print("Llamada al método getter")
		return self.__distancia

	# Función para definir el valor de _distancia
	@obtener_distancia.setter
	def definir_distancia(self, valor):
		if valor < 0:
			raise ValueError("No es posible convertir distancias menores a 0.")
		print("Llamada al método setter")
		self.__distancia = valor


def main():

	avion = Millas()
	avion.definir_distancia = 200
	print(avion.obtener_distancia)

if __name__ == '__main__':
    main()
