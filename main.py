import threading
from coordenador import Coordenador
import time

def main():
    total_nos = 5
    coordenador = Coordenador(total_nos)
    
    threading.Thread(target=coordenador.iniciar).start()

    time.sleep(10)
    coordenador.falhar_no(2)
    time.sleep(5)
    coordenador.recuperar_no(2)

if __name__ == "__main__":
    main()