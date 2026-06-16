import os
import pwd
import sys

# Garante que o Python encontre a pasta raiz do projeto no path
caminho = os.path.dirname(os.path.abspath(__file__))
raiz_projeto = os.path.dirname(caminho)
if raiz_projeto not in sys.path:
    sys.path.append(raiz_projeto)

# Importa o arquivo formatters de dentro da pasta utils localizada na raiz
from utils import formatters


def leitura_dados_processo(pid):
    try:
        caminho_stat = f"/proc/{pid}/stat"

        with open(caminho_stat, "r") as r:
            conteudo = r.read()

            parte_inicial = conteudo.split(')')
            pid_e_nome = parte_inicial[0].split('(')

            parte_pid = pid_e_nome[0].strip()
            parte_comando = pid_e_nome[1].strip()

            # Separa o restante dos dados numéricos pós-comando
            dados_restantes = parte_inicial[1].split()

            parte_status = dados_restantes[0]
            parte_nice = dados_restantes[16]

            # Esta linha agora vai receber a string com o tempo real calculado pelo starttime
            parte_time = formatters.calcular_tempo_execucao(dados_restantes)
            status_formatado_correto = formatters.formatar_status(parte_status)

            # Coleta o UID do dono do processo
            uid_processo = os.stat(caminho_stat).st_uid

            # Traduz o UID numérico para o nome real do usuário
            try:
                user_real = pwd.getpwuid(uid_processo).pw_name
            except KeyError:
                user_real = str(uid_processo)

            return {
                "Pid": parte_pid,
                "Comando": parte_comando,
                "Status": status_formatado_correto,
                "Nice": parte_nice,
                "Time": parte_time,
                "User": user_real
            }
    
    except (FileNotFoundError, IndexError, PermissionError):
        return None
        
    except Exception as erro:
        # Só printa no terminal se for um erro bizarro e totalmente desconhecido
        print(f"Erro inesperado no PID {pid}: {erro}")
        return None

def listagem_dados_processos():
    lista_processos = [] 
    
    try:
        for nome_dir in os.listdir("/proc"): 
            if nome_dir.isdigit(): 
                pid = int(nome_dir) 
                dados_processo = leitura_dados_processo(pid) 

                if dados_processo is not None:
                    lista_processos.append(dados_processo)
                    
    except Exception as e:
        print(f"Erro ao listar os processos: {e}")
        
    return lista_processos


