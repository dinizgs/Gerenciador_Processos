import os
import pwd
import psutil
from datetime import datetime


#Função para retornar o usuário logado
def obter_usuario():
    user = pwd.getpwuid(os.getuid()).pw_name
    return user


def calcular_tempo_execucao(dados_sobraram):
    try:
        #UTIME: Representa o tempo que a CPU passou executando instruções no espaço do usuário
        utime = int(dados_sobraram[11])
        #STIME: Representa o tempo que a CPU passou executando chamadas de sistema no espaço do kernel em nome do seu programa
        stime = int(dados_sobraram[12])

        total_ticks = utime +stime

        ticks_por_segundo = os.sysconf(os.sysconf_names['SC_CLKTCK'])

        segundos_totais = int(total_ticks / ticks_por_segundo)

        horas = segundos_totais // 3600
        minutos = (segundos_totais % 3600) // 60
        segundos = segundos_totais % 60

        return f"{horas:2d}:{minutos:2d}:{segundos:2d}"
    
    except Exception:
        return "00:00:00"

def leitura_dados_processo(pid, user): #O user como parâmetro faz referencia ao retorno da primeira função --> line 70
    try:
        with open(f"/proc/{pid}/stat","r") as r:
            conteudo = r.read()

            parte_inicial = conteudo.split(')')
            pid_e_nome = parte_inicial[0].split('(')

            parte_pid = pid_e_nome[0].strip()
            parte_comando = pid_e_nome[1].strip()

            dados_restantes = parte_inicial[1].split()

            parte_status = dados_restantes[0]
            parte_nice = dados_restantes[16]

            parte_time = calcular_tempo_execucao(dados_sobraram=dados_restantes)

            status_map = {
                'R' : 'Executando (Running)',
                'S' : 'Dormindo (Sleeping)',
                'D' : 'Espera Ininterupta (Uninterruptible Sleep)',
                'Z' : 'Zumbi (Zombie)',
                'T' : 'Parado/Bloqueado (Stopped)'

            }

            status_formatado_correto = status_map.get(parte_status,parte_status)
            #uid_processo = os.stat(f"/proc/{pid}/stat").st_uid (Essa linha foi de uma pesquisa e o gemini sugeriu, mas não entendi totalmente, se precisar, tiro o comentário)

            return {
                "pid" : parte_pid,
                "comando" : parte_comando,
                "status" : status_formatado_correto,
                "nice" : parte_nice,
                "time" : parte_time,
                "user" : user #Ai o user é usado aqui
            }
        
    except (FileNotFoundError, ProcessLookupError, PermissionError):
        return None


def listagem_dados_processos():
    lista_processos = [] #aqui vai armazenar os processos por ID, sendo convertidos sempre em digitos
    user = obter_usuario() #resgata o usuário logado
    
    try:
        for nome_dir in os.listdir("/proc"): #percorre a lista de diretórios fruto da biblioteca os
            if nome_dir.isdigit(): #filtra os diretórios somente para os que contém PID
                pid = int(nome_dir) #Consta PID como o iterador nome_dir
                dados_processo = leitura_dados_processo(pid, user) #chama a função com os parâmetros do PID e usuário dinâmicos

                if dados_processo is not None:
                    lista_processos.append(dados_processo)
    except Exception as e:
        print(f"Erro ao listar os processos: {e}")
    return lista_processos




