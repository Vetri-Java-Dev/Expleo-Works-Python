from configparser import ConfigParser

def getData(category, key):

    config = ConfigParser()
    config.read("./config.ini")

    return config.get(category, key)