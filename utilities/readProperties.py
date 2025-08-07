import configparser

config = configparser.RawConfigParser()
config.read("C:/Users/shinu/SeleniumFramework/Configurations/config.ini")

class ReadConfig:
    @staticmethod # used to access functions directly without creating class object
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod 
    def getUserName():
        username = config.get('common info','Username')
        return username


    @staticmethod
    def getPassword():
        password = config.get('common info','Password')
        return password