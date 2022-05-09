from ampalibe import Model


class Requete (Model):
  def __init__(self, conf):
    '''
    Connexion à la base
    '''
    Model.__init__(self, conf)

  @Model.verif_db
  def list_album(self):
    """
      Fonction pour récupérer la liste des albums
    """
    req = """
            SELECT id_album, nom_album, photo
            FROM album
          """
    self.cursor.execute(req)
    result = self.cursor.fetchall()
    self.db.commit()
    return result

  @Model.verif_db
  def list_music(self):
    """
       Fonction pour récupérer la liste des musiques
    """
    req="""
          SELECT id_chant, titre, photo_couverture
          FROM chansons
        """
    self.cursor.execute(req)
    result = self.cursor.fetchall()
    self.db.commit()
    return result

  @Model.verif_db
  def get_AlbumMusic(self, id_album):
    """
      Function pour récupérer la liste des musiques contenu dans un albums
    """
    req="""
          SELECT id_chant, titre, photo_couverture
          FROM chansons 
          WHERE idAlbum = %s  
        """

    self.cursor.execute(req, (id_album,)) 
    result = self.cursor.fetchall()
    self.db.commit()
    return result


  @Model.verif_db
  def list_tournee(self):
    """
      Récupération des prochaines tournées de l'artiste X
    """
    req="""
          SELECT id_tournee, date, heure, Lieu, image
          FROM tournee
        """

    self.cursor.execute(req)
    result = self.cursor.fetchall()
    self.db.commit()
    return result
     

  @Model.verif_db
  def get_audio(self, id_chant):
    """
      Récupération du musique audio de la chanson 
    """
    req="""
          SELECT media
          FROM media
          WHERE id_chanson= %s AND idType = 2
        """
    self.cursor.execute(req, (id_chant,))
    result = self.cursor.fetchone()
    self.db.commit()
    return result[0]


  @Model.verif_db
  def get_video(self, id_chant):
    """
      Récupération du musique vidéo de la chanson 
    """
    req="""
          SELECT media
          FROM media
          WHERE id_chanson= %s AND idType = 1
        """
    self.cursor.execute(req, (id_chant,))
    result = self.cursor.fetchone()
    self.db.commit()
    return result[0]


  @Model.verif_db
  def Music_Search(self, title):
    """
      Fonction pour trouver la musique recherhé par l'utilisateur
    """
    req="""
          SELECT id_chant, titre, photo_couverture
          FROM chansons
          WHERE UPPER(titre) LIKE %s
          OR SOUNDEX(titre)=SOUNDEX(%s)
        """
    self.cursor.execute(req, (f"%{title.upper()}%", title))
    result = self.cursor.fetchall()
    self.db.commit()
    return result
  
  @Model.verif_db
  def get_reservation(self, id_tournee):
    """
      Fonction pour vérifier la disponibilité selon la date de tournée
    """
    req="""
          SELECT id_reservation, date_debut, date_fin, nbre_billet
          FROM reservation
          WHERE id_tournee=%s
        """
    self.cursor.execute(req, (id_tournee,))
    result = self.cursor.fetchall()
    self.db.commit()
    return result

  
  @Model.verif_db
  def get_temp(self, user_id):
    '''
      Récuperer les données temporaire de l'utilisateur
    '''
    req = "SELECT tmp FROM amp_user"
    self.cursor.execute(req, (user_id))
    result = self.cursor.fetchone()
    self.db.commit()
    return result[0]

  