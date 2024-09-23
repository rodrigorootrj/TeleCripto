import requests
import telepot
class Telegram:
    def main():
        ...

    def sendMessage(text,token_telegram,telegram_group):
        # Insira seu token do bot aqui
        token = token_telegram
        # Insira o ID do canal aqui
        canal_id = telegram_group
        # Crie um objeto da classe `Bot`
        bot = telepot.Bot(token)
        # Envie a mensagem para o canal
        mensagem = text
        bot.sendMessage(canal_id, mensagem)
        return 200   

    def echo():
        print('class Telegram, path lib.telegram')

