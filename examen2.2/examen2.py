# Clase Persona
class Persona:
    def __init__(self, nombre: str, nif: str, fecha_nac: str):
        self.nombre = nombre
        self.nif = nif
        self.fecha_nac = fecha_nac

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"NIF: {self.nif}")
        print(f"Fecha de nacimiento: {self.fecha_nac}")


# Clase Jugador (hereda de Persona)
class Jugador(Persona):
    def __init__(self, nombre: str, nif: str, fecha_nac: str, num_fed: int):
        # Llamar al constructor de la clase padre (Persona)
        super().__init__(nombre, nif, fecha_nac)
        self.num_fed = num_fed

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Número de Federación: {self.num_fed}")


# Ejemplo de uso
if __name__ == "__main__":
    jugador1 = Jugador("Carlos Pérez", "12345678A", "1998-06-15", 4521)
    jugador1.mostrar_datos()




