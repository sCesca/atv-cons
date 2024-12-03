import random
import threading
import time

TEMPO_LIMITE_ELEICAO = 5
INTERVALO_HEARTBEAT = 1

class NoRaft:
    def __init__(self, id_no, nos):
        self.id_no = id_no
        self.estado = "Seguidor"
        self.votos_recebidos = 0
        self.id_lider = None
        self.nos = nos
        self.termo_atual = 0
        self.ultimo_heartbeat = time.time()
        self.ativo = True

    def enviar_heartbeat(self):
        while self.estado == "Lider" and self.ativo:
            print(f"No {self.id_no} (Lider) enviando heartbeat.")
            for no in self.nos:
                no.receber_heartbeat(self.id_no, self.termo_atual)
            time.sleep(INTERVALO_HEARTBEAT)

    def receber_heartbeat(self, id_lider, termo):
        if termo >= self.termo_atual:
            self.estado = "Seguidor"
            self.id_lider = id_lider
            self.termo_atual = termo
            self.ultimo_heartbeat = time.time()
            print(f"No {self.id_no} recebeu heartbeat do Lider {self.id_lider}.")

    def iniciar_eleicao(self):
        self.estado = "Candidato"
        self.termo_atual += 1
        self.votos_recebidos = 1
        print(f"No {self.id_no} iniciou eleicao para o termo {self.termo_atual}.")
        
        for no in self.nos:
            no.solicitar_voto(self)

        time.sleep(random.uniform(0, TEMPO_LIMITE_ELEICAO))

        if self.votos_recebidos > len(self.nos) // 2:
            self.estado = "Lider"
            print(f"No {self.id_no} eleito como Lider para o termo {self.termo_atual}.")
            threading.Thread(target=self.enviar_heartbeat).start()

    def solicitar_voto(self, no_candidato):
        if self.estado == "Seguidor" and no_candidato.termo_atual >= self.termo_atual:
            self.termo_atual = no_candidato.termo_atual
            self.estado = "Seguidor"
            no_candidato.votos_recebidos += 1
            print(f"No {self.id_no} votou no No {no_candidato.id_no} no termo {self.termo_atual}.")

    def executar(self):
        while self.ativo:
            if self.estado == "Seguidor" and time.time() - self.ultimo_heartbeat > TEMPO_LIMITE_ELEICAO:
                print(f"No {self.id_no} nao recebeu heartbeat, iniciando eleicao.")
                self.iniciar_eleicao()
            time.sleep(1)

    def falhar(self):
        self.ativo = False
        print(f"No {self.id_no} falhou.")

    def recuperar(self):
        self.ativo = True
        self.estado = "Seguidor"
        self.ultimo_heartbeat = time.time()
        print(f"No {self.id_no} recuperou.")