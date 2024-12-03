# Projeto Raft Simples

Este projeto implementa uma simulação simples do algoritmo de consenso Raft. O Raft é um algoritmo de consenso distribuído que permite que um conjunto de nós (servidores) concordem em um estado compartilhado, mesmo na presença de falhas.

## Descrição do Projeto

O projeto consiste em uma implementação básica do algoritmo Raft, onde os nós tomam decisões baseadas no protocolo Raft. A implementação inclui a eleição de líderes, envio de heartbeats, e simulação de falhas e recuperações dos nós.

## Estrutura do Projeto

- `no_raft.py`: Contém a classe `NoRaft` que representa um nó no algoritmo Raft.
- `coordenador.py`: Contém a lógica do nó coordenador e a gestão dos nós.
- `main.py`: Contém a função principal para executar a simulação.

## Rodar algoritmo

1. Clone o repositório:
   ```sh
   python main.py

## Explicação do Algoritmo
### Fases do Algoritmo

- Inicialização:
Cada nó é inicializado como um seguidor (Seguidor).
O coordenador cria e gerencia os nós.

- Envio de Heartbeats:
O líder envia heartbeats periodicamente para os seguidores para manter sua liderança.
Se um seguidor não receber um heartbeat dentro de um tempo limite (TEMPO_LIMITE_ELEICAO), ele inicia uma eleição.
Eleição:

Um nó que não recebe heartbeat se torna um candidato (Candidato) e inicia uma eleição.
O candidato solicita votos dos outros nós.
Se o candidato receber a maioria dos votos, ele se torna o líder (Lider).
Falhas e Recuperações:

Nós podem falhar e se recuperar durante a simulação.
O coordenador pode simular falhas e recuperações de nós específicos.

### Implementação
- no_raft.py

Classe NoRaft:
enviar_heartbeat: Envia heartbeats para os seguidores.
receber_heartbeat: Recebe heartbeats do líder.
iniciar_eleicao: Inicia uma eleição quando um nó não recebe heartbeats.
solicitar_voto: Solicita votos dos outros nós.
executar: Executa o ciclo principal do nó.
falhar: Simula a falha de um nó.
recuperar: Simula a recuperação de um nó.

- coordenador.py

Classe Coordenador:
iniciar: Inicia a execução dos nós.
falhar_no: Simula a falha de um nó específico.
recuperar_no: Simula a recuperação de um nó específico.

- main.py

Função main:
Cria e inicia o coordenador.
Simula a falha e recuperação de um nó específico.

### Possíveis Falhas Simuladas

- Falha de um Nó:

Um nó pode falhar durante a simulação, deixando de enviar e receber mensagens.
O coordenador pode simular a falha de um nó específico usando o método falhar_no.

- Recuperação de um Nó:

Um nó pode se recuperar após uma falha, retomando suas operações normais.
O coordenador pode simular a recuperação de um nó específico usando o método recuperar_no.

- Resposta do Sistema a Falhas
Quando um nó falha, ele deixa de participar do consenso até ser recuperado.
Se o líder falhar, os seguidores iniciarão uma nova eleição para eleger um novo líder.
Quando um nó se recupera, ele retoma suas operações como seguidor e pode participar de futuras eleições.
![image](https://github.com/user-attachments/assets/9044c177-f5b1-417f-87be-de04868cad83)

