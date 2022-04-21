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
            "payload": Payload("/menu", name='__album')
        },
        {
            "content_type": "text",
            "title": 'Liste chansons🎶',
            "payload": Payload("/menu", name='__chant')
        },
        {
            "content_type": "text",
            "title": 'Prochaines tournées🎤',
            "payload": Payload("/menu", name='__tournee')
        }
    ]
    chat.send_quick_reply(sender_id, quick_rep, 'Que souhaitez-vous faire?')

@ampalibe.command('/menu')
def album_data(sender_id, cmd, name, **extends):
    '''
        Fetching album data
    '''
    print(name)
    if name == '__album':
        albums = req.list_album()
        data = []
        i = 0
        while i < len(albums):
            button = [
                Button(
                    type="postback",
                    title="Details",
                    payload= Payload('__details'+ str(albums[i][0]))
                )
            ]
            data.append(
                Element(
                    title= str(i+1)+ "Album" + albums[i][1],
                    image_url= albums[i][2],
                    buttons= button,
                )
            )
            i = i + 1
        return data

        





