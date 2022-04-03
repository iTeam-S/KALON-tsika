from conf import DATABASE
import mysql.connector
from traceback import print_stack


class Requete:
  def __init__(self):
    '''
    Connexion à la base
    '''
    self.__connect()

  def __connect(self):
    self.db = mysql.connector.connect(**DATABASE)
    self.cursor = self.db.cursor()

  def verif_db(function):
    '''Vérification de la connexion'''
    def verif_connex(*arg, **kwarg):
      if not arg[0].db.is_connected:
        try:
          arg[0].db.reconnect()
        except Exception:
          arg[0].__connect()
      return function(*arg, **kwarg)
    return verif_connex
        
  @verif_db
  def list_music(self):
    req = """
            SELECT id, titre, photo, artiste
            FROM musique
          """
    self.cursor.execute(req)
    result = self.cursor.fetchall()
    self.db.commit()
    return result
