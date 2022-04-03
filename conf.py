from os import environ as env
from json import load


class Configuration:
    '''
        Retrieves the value from the environment.
        Takes the default value if not defined.
    '''
    ADAPTER = env.get('ADAPTER')

    DB_FILE = env.get('DB_FILE')



    # DATABASE=
    # {
    #     DB_HOST = env.get('DB_HOST', 'localhost')
    #     DB_USER = env.get('DB_USER', 'root')
    #     DB_PASSWORD = env.get('DB_PASSWORD', '')
    #     DB_PORT = env.get('DB_PORT', 3306)
    #     DB_NAME = env.get('DB_NAME')
    # }
    

    DATABASE ={
        'host' : 'localhost',
        'user':'root',
        'password':'',
        'port':3306,
        'database':'kalontsika'
    }


    # ACCESS_TOKEN = env.get('AMP_ACCESS_TOKEN')
    # VERIF_TOKEN = env.get('AMP_VERIF_TOKEN')

    ACCESS_TOKEN ='EAAKHlnGZCLx4BAIGCcZBTgodBhboNFAdySv73TbLrrnZAtiSg2Xn2FwTjwaREzwQV9106Gvryd0b0vwFrhahQVA9DRdlxRuAKP6ji8xNloQYqryad2K4aHQL9gSKY3QMRMbOqiLP9Wnjl47xVUjkfwPiBcVyXKp3p3SQTyzcZB1PhMd86Hg5'
    VERIF_TOKEN = 'KALOAPP'

    APP_HOST = env.get('AMP_HOST')
    APP_PORT = int(env.get('AMP_PORT'))
    APP_URL = env.get('AMP_URL')

