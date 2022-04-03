from ampalibe import Model


class Requete (Model):
  def __init__(self, conf):
    '''
    Connexion à la base
    '''
    Model.__init__(self, conf)

  @Model.verif_db
  def list_music(self):
    req = """
            SELECT id_musique, titre, photo, artiste
            FROM musique
          """
    self.cursor.execute(req)
    result = self.cursor.fetchall()
    self.db.commit()
    return result