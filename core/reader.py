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
        minutos = (segundos_totais & 3600) // 60
        segundos = segundos_totais & 60

        return f"{horas:2d}:{minutos:2d}:{segundos:2d}"
    
    except Exception:
        return "00:00:00"