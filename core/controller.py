import os
import signal
import subprocess
import sys

caminho = os.path.dirname(os.path.abspath(__file__))

raiz_projeto = os.path.dirname(caminho)

if raiz_projeto not in sys.path:
    sys.path.append(raiz_projeto)

from core import reader
from typing import Tuple


def bloquear_processo(pid):
    try:
        os.kill(int(pid), signal.SIGSTOP)
        return True
    
    except (ProcessLookupError, PermissionError):
        return False

def continuar_processo(pid):
    try:
        os.kill(int(pid), signal.SIGCONT)
        return True
    
    except (ProcessLookupError, PermissionError):
        return False

def finalizar_processo(pid):
    try:
        os.kill(int(pid), signal.SIGKILL)
        return True
    
    except (ProcessLookupError, PermissionError):
        return False
    
def executar_processo(comando_abrir_programa):
    try:
        subprocess.Popen(comando_abrir_programa, shell=True)
        return True

    except (FileNotFoundError):
        return False

def reiniciar_processo(pid):
    try:
        usuario_atual = reader.obter_usuario()
        dados_gerais = reader.leitura_dados_processo(pid,usuario_atual)

        if dados_gerais == None:
            return False
        
        parte_comando = dados_gerais.get("comando")

        finalizar_processo(pid)
        executar_processo(parte_comando)
        return True
    
    except (ProcessLookupError, PermissionError, FileNotFoundError, AttributeError):
        return False

def alterar_prioridade_execucao(pid,nice):
    try:
        os.setpriority(os.PRIO_PROCESS, int(pid), int(nice))
        return True
    
    #Se o processo sumir ou apagar
    except (ProcessLookupError):
        return False
    
    #Se o processo precisa de permissão de adm para mudar a prioridade
    except (PermissionError):
        return False