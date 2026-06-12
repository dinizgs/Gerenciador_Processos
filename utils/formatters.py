import os

def calcular_tempo_execucao(dados_sobraram):
    try:
        utime = int(dados_sobraram[11])
        stime = int(dados_sobraram[12])

        total_ticks = utime + stime
        ticks_por_segundo = os.sysconf(os.sysconf_names['SC_CLKTCK'])

        segundos_totais = int(total_ticks / ticks_por_segundo)

        horas = segundos_totais // 3600
        minutos = (segundos_totais % 3600) // 60
        segundos = segundos_totais % 60

        return f"{horas:02d}:{minutos:02d}:{segundos:02d}"
    except Exception:
        return "00:00:00"


def formatar_status(sigla_status):
    status_map = {
        'R' : '🟢 Executando (Running)',
        'S' : '🌙 Dormindo (Sleeping)',
        'D' : '⏳ Espera Ininterrupta (Dounded Sleep)',
        'Z' : '💀 Zumbi (Zombie)',
        'T' : '🛑 Parado/Bloqueado (Stopped)',
        'I' : '💤 Ocioso (Idle)'
    }
    return status_map.get(sigla_status, sigla_status)