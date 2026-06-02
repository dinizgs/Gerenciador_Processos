import os
import signal
import psutil
from typing import Tuple


def bloquear_processo(pid: int) -> Tuple[bool, str]:
    """
    Bloqueia um processo enviando SIGSTOP.

    Args:
        pid (int): ID do processo

    Returns:
        Tuple[bool, str]: (sucesso, mensagem)
    """
    try:
        os.kill(pid, signal.SIGSTOP)
        return True, f"Processo {pid} bloqueado com sucesso."
    except ProcessLookupError:
        return False, f"Processo {pid} não encontrado."
    except PermissionError:
        return False, f"Permissão negada para bloquear processo {pid}."
    except Exception as e:
        return False, f"Erro ao bloquear processo {pid}: {str(e)}"


def continuar_processo(pid: int) -> Tuple[bool, str]:
    """
    Continua um processo bloqueado enviando SIGCONT.

    Args:
        pid (int): ID do processo

    Returns:
        Tuple[bool, str]: (sucesso, mensagem)
    """
    try:
        os.kill(pid, signal.SIGCONT)
        return True, f"Processo {pid} continuado com sucesso."
    except ProcessLookupError:
        return False, f"Processo {pid} não encontrado."
    except PermissionError:
        return False, f"Permissão negada para continuar processo {pid}."
    except Exception as e:
        return False, f"Erro ao continuar processo {pid}: {str(e)}"


def terminar_processo(pid: int, graceful: bool = True) -> Tuple[bool, str]:
    """
    Termina um processo.

    Args:
        pid (int): ID do processo
        graceful (bool): Se True, tenta SIGTERM primeiro, depois SIGKILL. Se False, usa SIGKILL.

    Returns:
        Tuple[bool, str]: (sucesso, mensagem)
    """
    try:
        if graceful:
            os.kill(pid, signal.SIGTERM)
            try:
                psutil.wait_procs([psutil.Process(pid)], timeout=3)
            except psutil.TimeoutExpired:
                os.kill(pid, signal.SIGKILL)
                return True, f"Processo {pid} terminado à força (SIGKILL)."
        else:
            os.kill(pid, signal.SIGKILL)

        return True, f"Processo {pid} terminado com sucesso."
    except ProcessLookupError:
        return False, f"Processo {pid} não encontrado."
    except PermissionError:
        return False, f"Permissão negada para terminar processo {pid}."
    except Exception as e:
        return False, f"Erro ao terminar processo {pid}: {str(e)}"


def alterar_prioridade(pid: int, nice_value: int) -> Tuple[bool, str]:
    """
    Altera a prioridade de um processo (nice value).

    Args:
        pid (int): ID do processo
        nice_value (int): Novo valor nice (-20 a 19)

    Returns:
        Tuple[bool, str]: (sucesso, mensagem)
    """
    if nice_value < -20 or nice_value > 19:
        return False, f"Valor de nice deve estar entre -20 e 19. Recebido: {nice_value}"

    try:
        proc = psutil.Process(pid)
        proc.nice(nice_value)
        return True, f"Prioridade do processo {pid} alterada para {nice_value}."
    except ProcessLookupError:
        return False, f"Processo {pid} não encontrado."
    except PermissionError:
        return False, f"Permissão negada para alterar prioridade do processo {pid}."
    except Exception as e:
        return False, f"Erro ao alterar prioridade do processo {pid}: {str(e)}"


def obter_prioridade_atual(pid: int) -> Tuple[bool, int, str]:
    """
    Obtém o valor nice atual de um processo.

    Args:
        pid (int): ID do processo

    Returns:
        Tuple[bool, int, str]: (sucesso, nice_value, mensagem)
    """
    try:
        proc = psutil.Process(pid)
        nice_value = proc.nice()
        return True, nice_value, f"Nice value do processo {pid}: {nice_value}"
    except ProcessLookupError:
        return False, 0, f"Processo {pid} não encontrado."
    except PermissionError:
        return False, 0, f"Permissão negada para acessar processo {pid}."
    except Exception as e:
        return False, 0, f"Erro ao obter prioridade do processo {pid}: {str(e)}"
