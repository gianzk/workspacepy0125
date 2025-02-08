from config.database import *
from config.mail import *


class App:

    def __init__(self,path):
        stmp_server,port,user,password=[
                'sandbox.smtp.mailtrap.io',
                2525,
                '9a3c8223168f67',
                '367b96da6a548b'
                ]
        self.bd:Database=Database(path)        
        self.mail=Mail(stmp_server,port,user,password)
