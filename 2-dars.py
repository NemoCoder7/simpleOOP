# Singleton
class DataBase:
    __instance = None

    # def __new__(cls, *args, **kwargs):
    #     if cls.__instance is None:
    #         cls.__instance = super().__new__(cls)
    #     return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"Baza dannix ulandi: {self.user}, {self.port}")

    def close(self):
        print("Baza dannix bilan aloqa uzildi")

    def read(self):
        print("DB-dan ma'lumot o'qildi")

    def write(self, data):
        print(f"Db-ga {data} yozildi")


db = DataBase("user1", "pass1", 2000)
db2 = DataBase("user2", "pass2", 3000)
db.connect()
db2.connect()
