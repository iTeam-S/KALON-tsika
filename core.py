import ampalibe
from conf import Configuration
from ampalibe import Payload
from requete import Requete
from ampalibe.ui import Element, Button, QuickReply
from datetime import datetime

bot = ampalibe.init(Configuration())
chat = bot.chat
req = Requete(Configuration())
query = bot.query
temp = req.get_temp(1)
print(temp)
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
            "payload": Payload("/album")
        },
        {
            "content_type": "text",
            "title": 'Liste chansons🎶',
            "payload": Payload("/musique")
        },
        {
            "content_type": "text",
            "title": 'Prochaines tournées🎤',
            "payload": Payload("/tournee")
        }
    ]
    chat.send_quick_reply(sender_id, quick_rep, 'Que souhaitez-vous faire?')

@ampalibe.command('/album')
def get_album(sender_id, cmd, **extends):
    '''
        Fonction fetcher les données dans album et les afficher
    '''
    albums = req.list_album()
    data = []
    i = 0
    while i < len(albums):

        button = [
            Button(
                type="postback",
                title="Details",
                payload= Payload('/details', id_album = str(albums[i][0]))
            )
        ]
        data.append(
            Element(
                title= str(i+1)+ "- Album " + albums[i][1],
                image_url= albums[i][2],
                buttons= button,
            )
        )
        i = i + 1

    chat.send_template(sender_id, data, next=True)

    

@ampalibe.command('/musique')
def get_music(sender_id, cmd, **extends):
    '''
        Fonction fetcher les données dans musique et les afficher
    '''
    musiques = req.list_music()
    data = []
    i = 0
    while i < len(musiques):

        buttons = [
            Button(
                type="postback",
                title="Ecouter🎧/Télécharger⏳",
                payload= Payload('/listen', id_music= str(musiques[i][0]))
            ),
            Button(
                type="postback",
                title="Regarder🎬/Télécharger⏳",
                payload= Payload('/see', id_music= str(musiques[i][0]))
            )
        ]
        data.append(
            Element(
                title= str(i+1)+ "- "+ musiques[i][1],
                image_url= musiques[i][2],
                buttons= buttons,
            )
        )
        i = i + 1

    chat.send_template(sender_id, data, next=True)
    query.set_action(sender_id, None)


@ampalibe.command('/tournee')
def get_tournee(sender_id, cmd, **extends):
    '''
        Fonction fetcher les données dans album et les afficher
    '''
    tournee = req.list_tournee()
    data = []
    i = 0
    while i < len(tournee):

        button = [
            Button(
                type="postback",
                title="Plus d'information",
                payload= Payload('/info', id_tournee = str(tournee[i][0]))
            )
        ]
        data.append(
            Element(
                title= str(i+1)+ "- Le " + str(tournee[i][1]) + " à " + str(tournee[i][2]) + " au " + tournee[i][3],
                image_url= tournee[i][4],
                buttons= button,
            )
        )
        i = i + 1

    chat.send_template(sender_id, data, next=True)


#--------------------------------------*Traitement des paload musique-----------------------------------------------------------#
@ampalibe.command('/see')
def get_Video(sender_id, id_music, **extends):
    """
        Fonction pour récupérer la musique vidéo
    """

    video_name = req.get_video(id_music)
    print(video_name)
    chat.send_message(sender_id, "Enjoy it!!!")
    chat.send_file_url(sender_id, Configuration.APP_URL+f"/asset/{video_name}", filetype='video')


@ampalibe.command('/listen')
def get_Audio(sender_id, id_music, **extends):
    """
        Fonction pour récupérer la musique audio
    """

    audio_name = req.get_audio(id_music)
    print(audio_name)
    chat.send_message(sender_id, "Enjoy it!!!")
    chat.send_file_url(sender_id, Configuration.APP_URL+f"/asset/{audio_name}", filetype='audio')


#-------------------------------------------------------------*Traitement de l'album*--------------------------------------------------------#
@ampalibe.command('/details')
def get_details(sender_id, id_album, **extends):
    """
        Fonction pour afficher la liste des musique contenu dans l'album
    """
    chansons = req.get_AlbumMusic(id_album)
    print(chansons)

    data = []
    i = 0
    while i < len(chansons):
        buttons = [
            Button(
                type="postback",
                title="Ecouter🎧/Télécharger⏳",
                payload= Payload('/listen', id_music= str(chansons[i][0]))
            ),
            Button(
                type="postback",
                title="Regarder🎬/Télécharger⏳",
                payload= Payload('/see', id_music= str(chansons[i][0]))
            )
        ]
        data.append(
           Element(
               title= str(i+1) + "- " + chansons[i][1],
               image_url= chansons[i][2],
               buttons = buttons
           )
        )
        i = i + 1
    chat.send_message(sender_id, "Voilà donc les chansons contenu dans cet album")
    chat.send_template(sender_id, data, next=True)
    


#---------------------------------------------------------*Traitement tournée*------------------------------------------------------------------#
@ampalibe.command('/info')
def get_information(sender_id,id_tournee, **extends):
    """
        Fonction pour donner les information sur la réservation
    """
    disponibilite = req.get_reservation(id_tournee)
    i = 0

    chat.send_message(sender_id, "Voià les informations pour réserver: ")
    chat.send_message(sender_id, " 📑Debut de réservation: "+ str(disponibilite[i][1]) + " -📑Fin de réservation: " + str(disponibilite[i][2]) + " -📑Nombre de billet disponible" + str(disponibilite[i][3]))
    buttons = [
        Button(
            type='postback',
            title='OUI',
            payload=Payload('/reserver', id_res=id_tournee)
        ),
        Button(
            type='postback',
            title='NON',
            payload=Payload('/annuler', id_res=id_tournee)
        )
    ]
    chat.send_button(sender_id, buttons, "Voulez-vous continuer?")


@ampalibe.command('/reserver')
def get_reservation(sender_id, id_res, **extends):
    disponibilite = req.get_reservation(id_res)

    i = 0
    date_debut = disponibilite[i][1]
    date_fin = disponibilite[i][2]
    nbr_billet = disponibilite[i][3]
    
    if datetime.now() >= date_debut:
        if datetime.now() <= date_fin:
            if nbr_billet >= 1:
                print("Reservation")

                chat.send_message(sender_id, "Pour pouvoir valider votre réservation, il faudrait passer au payement!!!")
                quick_rep = [
                    QuickReply(
                        title = 'Orange',
                        payload = Payload('/orange', id_musics = id_res)
                    ),
                    QuickReply(
                        title = 'Telma',
                        payload = Payload('/telma', id_musics = id_res)
                    )
                ]
                chat.send_quick_reply(sender_id, quick_rep, "Operateur")

            else:
                chat.send_message(sender_id, "Désolé, guichet fermé!!")
        else:
           chat.send_message(sender_id, "La date de réservation est déjà expiré, meri de votre intérêt!!")

    else:
       chat.send_message(sender_id, "Veuillez attendre le date début de réservation" + str(date_debut))



