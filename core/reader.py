import os
import pwd
import psutil
from datetime import datetime


#Função para retornar o usuário logado
def obter_usuario():
    return pwd.getpwuid(os.getuid()).pw_name


def calcular_tempo_execucao(dados_sobraram):
    try:
        #UTIME: Representa o tempo que a CPU passou executando instruções no espaço do usuário
        utime = dados_sobraram[11]
        #STIME: Representa o tempo que a CPU passou executando chamadas de sistema no espaço do kernel em nome do seu programa
        stime = dados_sobraram[12]

        total_ticks = utime +stime

        ticks_por_segundo = os.sysconf(os.sysconf_names['SC_CLKTCK '])

        segundos_totais = int(total_ticks / ticks_por_segundo)

        horas = segundos_totais / 3600
        minutos = (segundos_totais % 3600) // 60
        segundos = segundos_totais % 60

        return f"{horas:2d}:{minutos:2d}:{segundos:2d}"
    
    except Exception:
        return "00:00:00"

def leitura_dados_processo():
    try:
        with open("/proc/[PID]/stat","r") as r:
            conteudo = r.read()

            parte_inicial = conteudo.split(')')
            pid_e_nome = parte_inicial[0].split('(')

            parte_pid = pid_e_nome[0].strip()
            parte_comando = pid_e_nome[1].strip()

            dados_restantes = parte_inicial[1].split()

            parte_status = dados_restantes[0]
            parte_nice = dados_restantes[15]

            parte_time = calcular_tempo_execucao(dados_sobraram=dados_restantes)

            status_map = {
                'R' : 'Executando (Running)',
                'S' : 'Dormindo (Sleeping)',
                'D' : 'Espera Ininterupta',
                'Z' : 'Zumbi (Zombie)',
                'T' : 'Parado/Bloqueado (Stopped)'

            }

            status_formatado_correto = status_map.get(parte_status,parte_status)

            return {
                "pid" : parte_pid,
                "comando" : parte_comando,
                "status" : parte_status,
                "nice" : parte_nice,
                "time" : parte_time,
                "user" : ""
            }
        
    except (FileNotFoundError, ProcessLookupError, PermissionError):
        return None



