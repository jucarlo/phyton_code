#listas, tuplas, diccionarios, booleanos y estructuras de control.
#1.Añadir un contacto: Crear un nuevo registro en la agenda (nombre, telefono).
#2.Buscar un contacto: Buscar un contacto por nombre y mostrar su teléfono, o un mensaje de error si no lo encuentra.
#3.Editar un contacto: Modificar teléfono de un contacto existente.
#4.Eliminar un contacto: Eliminar un contacto de la agenda (investiga los métodos disponibles para lograrlo)
#5.Mostrar todos los contactos: Mostrar todos los contactos guardados en la agenda.

name = ""
phone = 0
contacts = {"a":11,"b":22,"c":33}


while True:
    print("---------------------")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Edit contact")
    print("4. Delete contact")
    print("5. Show all contacts")
    print("6. Exit")
    print("---------------------")
    opcion = int(input("Choose an opcion: "))
    print("You choosed opcion numer " + str(opcion))

    if opcion == 1:
        name = input("Name: ")
        phone = input("Phone: ")
        contacts.update({name:phone})
    if opcion == 2:
        name = input("Name to search: ")
        if name in contacts:
            print(f"phone number of '{name}' is {contacts[name]}")
        else:
            print(f"'{name}' does not exist")
    if opcion == 3:
        name = input("contact name: ")
        if name in contacts:
            phone = input("Phone to update: ")
            contacts[name] = phone
            print("Phone was updated!")
        else:
            print(f"'{name}' does not exist")
    if opcion == 4:
        name = input("contact name to remove: ")
        if name in contacts:
            contacts.pop(name)
            print("Contact removed")
        else:
            print(f"'{name}' does not exist")
    if opcion == 5:
        print("Here is all contact list")
        print(contacts)
        
    if opcion == 6:
        break