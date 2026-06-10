from configparser import ConfigParser

def get_value(filename,category, key):
    config=ConfigParser()
    config.read("./Configuration/"+filename)
    return config.get(category, key)