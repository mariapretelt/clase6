from datetime import datetime

class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV:
    def __init__(self):
        self.__lista_mascotas = []
        self.__caninos= {}
        self.__felinos= {}
    
    def verificarExiste(self,historia):
        for m in self.__lista_mascotas:
            if historia == m.verHistoria():
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False
        
    def verNumeroMascotas(self): 
        return len(self.__lista_mascotas) 

    def ingresarMascota(self,mascota):#clasificar canino o felino
        self.__lista_mascotas.append(mascota) 
        historia = mascota.verHistoria()
        tipo = mascota.verTipo().lower()

        if tipo == 'canino':
            self.__caninos[historia] = mascota
        elif tipo == 'felino':
            self.__felinos[historia] = mascota

    def verCaninos(self):
        return self.__caninos

    def verFelinos(self):
        return self.__felinos

    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verLista_Medicamentos() 
        return None
    
    def eliminarMedicamento(self, historia, nombre_medicamento):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                lista_med = masc.verLista_Medicamentos()
                for med in lista_med:
                    if med.verNombre().lower() == nombre_medicamento.lower():
                        lista_med.remove(med)
                        return True
                return False 
        return None  
    
    def eliminarMascota(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                self.__lista_mascotas.remove(masc)  #opcion con el pop

                tipo= masc.verTipo().strip().lower()
                if tipo == 'canino' and historia in self.__caninos:
                    del self.__caninos[historia]

                elif tipo == "felino" and historia in self.__felinos:
                    del self.__felinos[historia]
                return True  #eliminado con exito
        return False 
    
def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Ver lista de caninos 
                       \n7- Ver lista de felinos 
                       \n8- Eliminar medicamento
                       \n9- Salir
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo=input("Ingrese el tipo de mascota (felino o canino): ")
                peso=int(input("Ingrese el peso de la mascota: "))

                while True:
                    fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ") #modificar
                    try:
                        datetime.strptime(fecha, "%d/%m/%Y")
                        break
                    except ValueError:
                        print('Ingrese formato correcto')

                nm=int(input("Ingrese cantidad de medicamentos: "))
                lista_med=[] 

                for i in range(0,nm):
                    nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                    #verificar que el nombre de los medicamentos no se repita 
                    if any(med.verNombre().lower() == nombre_medicamentos.lower() for med in lista_med):
                        print('Ya existe medicamento con este nombre. Porfavor ingrese uno diferente')
                        pass 
                    dosis =int(input("Ingrese la dosis: "))
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamentos)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)

                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)

            else:
                print("Ya existe la mascota con el numero de histoira clinica")

        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")
        
        elif menu==6:
            caninos = servicio_hospitalario.verCaninos()
            if caninos:
                print("\nMascotas caninas registradas:")
                for historia, mascota in caninos.items():
                    print(f"- Historia: {historia}, Nombre: {mascota.verNombre()}")
            else:
                print('No se registran caninos')
            
        elif menu == 7:  
            felinos = servicio_hospitalario.verFelinos()
            if felinos:
                print("\nMascotas felinas registradas:")
                for historia, mascota in felinos.items():
                    print(f"- Historia: {historia}, Nombre: {mascota.verNombre()}")
            else:
                print('No se registran felinos')

        elif menu == 8:  # Eliminar medicamento de una mascota
            historia = int(input("Ingrese la historia clínica de la mascota: "))
            nombre_medicamento = input("Ingrese el nombre del medicamento a eliminar: ")
            resultado = servicio_hospitalario.eliminarMedicamento(historia, nombre_medicamento)

            if resultado == True:
                print('Medicamento eliminado')
            elif resultado == False:
                print('No se encontró medicamento en la lista')
            else:
                print('No se encontró mascota con esa historia clínica')

        elif menu==9:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()





            

                

