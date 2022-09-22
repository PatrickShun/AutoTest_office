import configparser

cf = configparser.ConfigParser()
cf.read(r"Myconfig.ini", encoding='utf-8')

print(cf.get('sec_a','a_key1'))

