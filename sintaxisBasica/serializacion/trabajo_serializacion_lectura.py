import pickle

fichero = open("name_list", "rb")

name_list = pickle.load(fichero)

fichero.close()

print(name_list)