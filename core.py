import ampalibe
from conf import Configuration
from ampalibe import Payload
from requete import Requete

bot = ampalibe.init(Configuration())
chat = bot.chat
req = Requete(Configuration())


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
            "payload": "RECHERCHER"
        },
        {
            "content_type": "text",
            "title": 'Voir les playlists🎶',
            "payload": "LISTES"
        }
    ]
    chat.send_quick_reply(sender_id, quick_rep, 'Que souhaitez-vous faire?')



def Music_lists(self):
    #----------------------------*$*---------------------------------------#
    #                    Fetching all data from our database        
    #-----------------------------*$*--------------------------------------#
    self.data = req.list_music()
    musics=[]
    i=0
    while i<len(self.data):
        musics.append({
            "title":str(self.data[i][0]+ "-" + self.data.[i][1]),
            "image_url":self.data[i][2],
            "subtitle":"Artiste:" + str(self.data[i][3]),
            "buttons":[
                {
                    "type":"postback",
                    "title":"Regarder et écouter",
                    "payload":"VOIR"+" "+str(self.data[i][0])
                },
                {
                    "type":"postback",
                    "title":"Télécharger",
                    "payload":"DOWNLOAD"+" "+str(self.data[i][0])
                }
            ]
        })
        i+=1
    return musics