
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import web

#Habilita el login
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

#Conexion a base de datos
db = web.database(
    dbn = 'mysql',
    host = 'localhost',
    db = 'Mybot',
    user = 'Hatsune',
    pw = 'Miku',
    port = 3306
    )

#Token Miku 
token = '712748838:AAExzosbeM6lMHJxAa_vUFWr4zELH1eRZvE'


def start(bot, update):
    username = update.message.from_user.username
    update.message.reply_text('Hola {} usa estos comandos:\n/Recomendaciones (Aqui va el numero del genero) #Estas aburrido?  \n/help (Comandos que puedes usar)'.format(username))

def help(bot, update):
    username = update.message.from_user.username
    update.message.reply_text('Hola {} usa estos comandos:\n/Recomendaciones #Buscas recomendaciones de anime? \n/info (Informacion sobre mi)'.format(username))

def search(update):
    text = update.message.text.split()
    username = update.message.from_user.username
    try:
        
        genero = int(text[1])
        print "Enviando informacion a {}".format(username)
        print "Busqueda de Genero {}".format(genero)
        result = db.select('Recomandaciones', where='Genero=$genero', vars=locals())[0]
        print result
        respuesta =  str(result.Anime) + ", " + str(result.Capitulos) + ", " + str(result.Emision)
        #imprime respuesta
        update.message.reply_text('Hola {}\nEsta es mi recomendaciones del genero {} :\n{}'.format(username, genero, respuesta))
    except Exception as e:
        print "Error: " + str(e.message)
        update.message.reply_text('Ok estos son los generos de anime \n 1.-Shounen (Peleas) \n 2.-Gore (Sangre y viceras) \n 3.-Shoujo (Romance) \n 4.-Comedia \n 5.-Mecha (Robots gigantes) \n 6.-Komodo (Criaturas magicas) \n 7.-Isekai (Otro Mundo) \n 8.-Mentantein (Policial) \n 9.-Spokon (Deportes)')
        update.message.reply_text('El genero no existe, revisa la lista de generos')  
def info(bot, update):
    username = update.message.from_user.username
    update.message.reply_text('Hola {} soy una mini bot que fue creada para ayudarte a encontrar una recomendacion de series de anime, de acuerdo con el genero dado'.format(username))
def Recomendaciones(bot, update):
    search(update)

def echo(bot, update):
    update.message.reply_text(update.message.text)
    print update.message.text
    print update.message.date
    print update.message.from_user
    print update.message.from_user.username
    
def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

    
def main():
    try:
        print 'Miku_bot Token'
        
        updater = Updater(token)

        
        dp = updater.dispatcher

        print 'Miku init dispatcher'

        # comandos de respuesta en Telegram
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))
        dp.add_handler(CommandHandler("Recomendaciones", Recomendaciones))
        dp.add_handler(CommandHandler("info", info))

        # mensaje echo Telegram
        dp.add_handler(MessageHandler(Filters.text, echo))

        # TRodos los errores de logueo
        dp.add_error_handler(error)

        # Inicia el bot
        updater.start_polling()

        # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        print 'Miku esta lista para ayudarle'
        updater.idle()
    except Exception as e:
        print "Error 100: ", e.message

if __name__ == '__main__':
    main()
