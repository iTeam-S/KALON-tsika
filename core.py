import ampalibe
from conf import Configuration

bot = ampalibe.init(Configuration())


@ampalibe.command('/')
def main(sender_id, cmd, **extends):
    bot.chat.send_message(sender_id,"Bonjour, bienvenu sur mon espace privée!!")
    96 
