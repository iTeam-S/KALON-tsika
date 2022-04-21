import ampalibe
from conf import Configuration
from ampalibe import Payload
from requete import Requete
from ampalibe.ui import Element, Button

bot = ampalibe.init(Configuration())
chat = bot.chat
req = Requete(Configuration())
query = bot.query
print(req.list_album())

@ampalibe.command('/')
def main(sender_id, cmd, **extends):
    #----------------------------*$*---------------------------------------#
    #                    Greeting ang giving the first menu        
    #-----------------------------*$*--------------------------------------#
    chat.send_message(sender_id,"Hello hello😍😘😘😘, bienvenu dans cette espace où je vais vous partager ma musique.")
    chat.send_message(sender_id, " Bon ambiance 💖!!!")
    quick_rep = [
        {
            "content_type": "text",
            "title": 'Listes albums📀',
            "payload": Payload("__album")
        },
        {
            "content_type": "text",
            "title": 'Liste chansons🎶',
            "payload": Payload("__chant")
        },
        {
            "content_type": "text",
            "title": 'Prochaines tournées🎤',
            "payload": Payload("__tournee")
        }
    ]
    chat.send_quick_reply(sender_id, quick_rep, 'Que souhaitez-vous faire?')

def album_data(self):
    '''
        Fetching album data
    '''
    albums = req.list_album()
    data = []
    i = 0
    while i < len(albums):
        buttons = [
            Button(
                type="postback",
                title="Details",
                payload= Payload('__details'+ str(data[i][0]))
            )
        ]
        data.append(
            Element(
                title= str(i+1)+ "Album" + data[i][1],
                image_url= data[i][2],
                buttons= buttons,
            )
        )
    i++
    return data

def albums_lists(self, sender_id, data):
    """
        Fonction pour afficher la liste des albums
    """
    album = data

    if album:
        """
            Mettre en place un système de pagination pour éviter les erreur
            envoyé par Messenger si la liste excède de 10.
            Sachant que l'indice initiale est 0
        """

        indice_init = 0

        """
        Puis vérifions si la liste des albums sont encore supérieur à indice_init+10 pour mettre à la page suivante
        """
        if len(album) > indice_init + 10:
            chat.send_template(sender_id, album[indice_init:indice_init + 10], next=True)
        
        else:
            chat.send_template(sender_id, album[indice_init:indice_init + 10])
        
    else:
        chat.send_message(sender_id, "J'ai pas encore sorti d'album pour l'instant")




