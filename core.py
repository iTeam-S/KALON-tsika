import ampalibe
from conf import Configuration
from ampalibe import Payload

bot = ampalibe.init(Configuration())
chat = bot.chat


@ampalibe.command('/')
def main(sender_id, cmd, **extends):
    #----------------------------*$*---------------------------------------#
    #                    Greeting ang giving the first menu        
    #-----------------------------*$*--------------------------------------#
    chat.send_message(sender_id,"Bonjour, bienvenu sur mon espace privée!!")
    quick_rep = [
        {
            "content_type": "text",
            "title": 'Rechercher 🎼',
            "payload": Payload("Rechercher")
        },
        {
            "content_type": "text",
            "title": 'Voir les playlists🎶',
            "payload": Payload("Listes")
        }
    ]
    chat.send_quick_reply(sender_id, quick_rep, 'Que souhaitez-vous faire?')

