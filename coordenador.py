import threading
from no_raft import NoRaft

class Coordenador:
    def __init__(self, total_nos):
        self.nos = [NoRaft(id_no=i, nos=[]) for i in range(total_nos)]
        for no in self.nos:
            no.nos = [n for n in self.nos if n != no]

    def iniciar(self):
        threads = []
        for no in self.nos:
            t = threading.Thread(target=no.executar)
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

    def falhar_no(self, id_no):
        self.nos[id_no].falhar()

    def recuperar_no(self, id_no):
        self.nos[id_no].recuperar()