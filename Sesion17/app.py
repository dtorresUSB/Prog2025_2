import serial
import time

# Configura el puerto serie (ajusta el nombre del puerto según tu sistema)
puerto = 'COM5'  
baudios = 9600

try:
    # Abre la conexión serial
    ser = serial.Serial(puerto, baudios, timeout=1)
    time.sleep(2)  # Espera a que el puerto esté listo

    print(f"Leyendo datos desde {puerto} a {baudios} baudios...\nPresiona Ctrl+C para detener.")

    while True:
        if ser.in_waiting > 0:
            linea = ser.readline().decode('utf-8').strip()
            print(f"Recibido: {linea}")

except serial.SerialException as e:
    print(f"Error al abrir el puerto serie: {e}")

except KeyboardInterrupt:
    print("\nLectura detenida por el usuario.")

finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Puerto serie cerrado.")
