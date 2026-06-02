import os
import pwd
import psutil
from datetime import datetime


#Função para retornar o usuário logado
def obter_usuario():
    return pwd.getpwuid(os.getuid()).pw_name
