import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from DataConnectionLayer.iDbConfig import IConnection


class DbConfig(IConnection):
    def GetConnection(self):

        Consrt =""
        f = open('Config.json')
        data = json.load(f)

        for key, value in data['ConnectionStrings'].items():
            Consrt = value

        f.close()

        engine = create_engine(Consrt, echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
    pass

   

