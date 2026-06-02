import os
import pwd

def obter_usuario():
    return pwd.getpwuid(os.getuid()).pw_name

