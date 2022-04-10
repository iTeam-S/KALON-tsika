from ampalibe import Model


class Requete (Model):
  def __init__(self, conf):
    '''
    Connexion à la base
    '''
    Model.__init__(self, conf)

  @Model.verif_db
  def list_album(self):
    req = """
            SELECT id_album, nom_album, photo
            FROM album WHERE id_artiste = 3
          """
    self.cursor.execute(req)
    result = self.cursor.fetchall()
    self.db.commit()
    return result

  @Model.verif_db
  def list_music(self):
    req="""
          SELECT id_chant, titre, photo_couverture
          FROM chansons
        """
    self.cursor.execute(req)
    result = self.cursor.fetchall()
    self.db.commit()
    return result

  @Model.verif_db
  def list_musicAlbum(self, id_album):
    req="""
          SELECT id_chant, titre, photo_couverture
          FROM chansons 
          WHERE id_album = %s  
        """

    self.cursor.execute(req, (id_album)) 
    result = self.cursor.fetchall()
    self.db.commit()
    return result

     



  