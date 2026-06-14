import os

def calcular_tempo_execucao(dados_sobraram):
    try:
        # 1. Lê o uptime total do sistema em segundos (quanto tempo a máquina está ligada)
        with open("/proc/uptime", "r") as f:
            uptime_sistema = float(f.readline().split()[0])

        # 2. Captura o 'starttime' (índice 19 que corresponde ao campo 22 do /proc/[pid]/stat)
        starttime_ticks = float(dados_sobraram[19])

        # 3. Descobre a frequência de clock do sistema (geralmente 100 Hz no Linux)
        ticks_por_segundo = os.sysconf(os.sysconf_names['SC_CLK_TCK'])

        # 4. Converte o momento de inicialização do processo de 'ticks' para segundos reais
        tempo_inicio_segundos = starttime_ticks / ticks_por_segundo

        # 5. Calcula o tempo real decorrido (Tempo do Sistema - Momento em que o processo nasceu)
        segundos_totais = int(uptime_sistema - tempo_inicio_segundos)

        # Trata pequenas variações/atrasos milissegundos de leitura para não dar negativo
        if segundos_totais < 0:
            segundos_totais = 0

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