import os
import sys
sys.path.append("..")
import configparser
config = configparser.ConfigParser()
config.read('etcd/app.config')
##
token = config.get('default', 'token')
group = config.get('default', 'group')
###
## Criando um objeto com as credenciais.
class ArtifactConfig:
    def objMain():
        artefato = {
            'token' : os.environ.get('TELECRIPTO_TELEGRAM_TOKEN', token),
            'group' : os.environ.get('TELECRIPTO_TELEGRAM_GROUP', group),
            }
        return artefato