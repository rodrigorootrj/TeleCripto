import os
import sys
sys.path.append("..")
import configparser
config = configparser.ConfigParser()
config.read('etcd/app.config')
##
token = config.get('default', 'token')
url = config.get('default', 'url')
wtoken = config.get('worker', 'token')
###
## Criando um objeto com as credenciais.
class ArtifactConfig:
    def objMain():
        artefato = {
            'token' : os.environ.get('LOCAL_TOKEN', token),
            'url' : url,
            'pop_url' : wtoken
            }
        return artefato