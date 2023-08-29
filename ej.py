import signal
import time

def controlador_de_senales(signum, frame):
    print("Se recibió la señal SIGALRM. Reiniciando el temporizador...")
    signal.alarm(5)

signal.signal(signal.SIGALRM, controlador_de_senales)
signal.alarm(5)

print("Ejecutando el programa. La señal SIGALRM se enviará cada 5 segundos...")
while True:
    time.sleep(1)
