# VIEWS
from views.keyboard import KeyboardView
from views.mouse import MouseView
from views.speaker import SpeakerView
from views.computer import ComputerView
from views.monitor import MonitorView

# APP
def app():

    # VIEWS
    mouse_view = MouseView()
    keyboard_view = KeyboardView()
    monitor_view = MonitorView()
    speaker_view = SpeakerView()
    computer_view = ComputerView()

    while True:
        
        # OPTIONS TYPES DEVICES
        print("\n1. Computadores")
        print("2. Dispositivos de Entrada")
        print("3. Dispositivos de Salida")
        print("4. Ingresar cualquier tecla para salir.\n")

        try:
            option = input("Ingrese una opción: ")
            option = int(option)

            if option == 1:

                # COMPUTERS
                print("\n1. Crear computador")
                print("2. Listar computadores")
                print("3. Obtener computador por id")
                print("4. Actualizar computador")
                print("5. Eliminar computador")
                print("6. Ingresa cualquier tecla para salir.\n")

                option = input("Ingrese una opción: ")
                option = int(option)

                if option == 1:
                    computer_view.create_computer()
                elif option == 2:
                    computer_view.get_computers()
                elif option == 3:
                    computer_view.get_computer()
                elif option == 4:
                    computer_view.update_computer()
                elif option == 5:
                    computer_view.delete_computer()
                else:
                    break

            elif option == 2:

                # INPUT DEVICES
                print("\n1. Mouses")
                print("2. Teclados")
                print("3. Ingresar cualquier tecla para salir.\n")

                option = input("Ingrese una opción: ")
                option = int(option)

                if option == 1:

                    # MOUSES
                    print("\n1. Crear mouse")
                    print("2. Listar mouses")
                    print("3. Obtener mouse por id")
                    print("4. Actualizar mouse")
                    print("5. Eliminar mouse")
                    print("6. Ingresa cualquier tecla para salir.\n")

                    option = input("Ingrese una opción: ")
                    option = int(option)

                    if option == 1:
                        mouse_view.create_mouse()
                    elif option == 2:
                        mouse_view.get_mouses()
                    elif option == 3:
                        mouse_view.get_mouse()
                    elif option == 4:
                        mouse_view.update_mouse()
                    elif option == 5:
                        mouse_view.delete_mouse()
                    else:
                        break
                elif option == 2:

                    # KEYBOARDS
                    print("\n1. Crear teclado")
                    print("2. Listar teclados")
                    print("3. Obtener teclado por id")
                    print("4. Actualizar teclado")
                    print("5. Eliminar teclado")
                    print("6. Ingresa cualquier tecla para salir.\n")

                    option = input("Ingrese una opción: ")
                    option = int(option)

                    if option == 1:
                        keyboard_view.create_keyboard()
                    elif option == 2:
                        keyboard_view.get_keyboards()
                    elif option == 3:
                        keyboard_view.get_keyboard()
                    elif option == 4:
                        keyboard_view.update_keyboard()
                    elif option == 5:
                        keyboard_view.delete_keyboard()
                    else:
                        break

                else:
                    break
                
            elif option == 3:

                # OUTPUT DEVICES
                print("\n1. Monitor")
                print("2. Altavoz")
                print("3. Ingresa cualquier tecla para salir.\n")

                option = input("Ingrese una opción: ")
                option = int(option)

                if option == 1:

                    # MONITORS
                    print("\n1. Crear monitor")
                    print("2. Listar monitores")
                    print("3. Obtener monitor por id")
                    print("4. Actualizar monitor")
                    print("5. Eliminar monitor")
                    print("6. Ingresa cualquier tecla para salir.\n")

                    option = input("Ingrese una opción: ")
                    option = int(option)

                    if option == 1:
                        monitor_view.create_monitor()
                    elif option == 2:
                        monitor_view.get_monitors()
                    elif option == 3:
                        monitor_view.get_monitor()
                    elif option == 4:
                        monitor_view.update_monitor()
                    elif option == 5:
                        monitor_view.delete_monitor()
                    else:
                        break

                elif option == 2:

                    # SPEAKERS
                    print("\n1. Crear speaker")
                    print("2. Listar speakers")
                    print("3. Obtener speaker por id")
                    print("4. Actualizar speaker")
                    print("5. Eliminar speaker")
                    print("6. Ingresa cualquier tecla para salir.\n")

                    option = input("Ingrese una opción: ")
                    option = int(option)

                    if option == 1:
                        speaker_view.create_speaker()
                    elif option == 2:
                        speaker_view.get_speakers()
                    elif option == 3:
                        speaker_view.get_speaker()
                    elif option == 4:
                        speaker_view.update_speaker()
                    elif option == 5:
                        speaker_view.delete_speaker()
                    else:
                        break
                    
                else:
                    break

            else:
                break

        except Exception as e:
            print("Ingrese un número valido.")