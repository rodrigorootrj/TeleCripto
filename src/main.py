from lib.telegram import Telegram
from lib.config import ArtifactConfig
import time
def run():
    texto = 'WORK'
    value = ArtifactConfig.objMain()  
    token = value['token']
    group = value['group']
    Telegram.sendMessage(texto,token,group)
    time.sleep(60)
    return 200

if __name__ == '__main__':
    while True:
        run()