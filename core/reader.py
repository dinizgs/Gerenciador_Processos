import os
import pwd
import psutil
from datetime import datetime


def obter_usuario():
    """Retorna o usuário logado atual."""
    return pwd.getpwuid(os.getuid()).pw_name
