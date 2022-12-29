import pickle

name_list = ["Nana", "Lilo", "Ana", "Jenny"]

binary_file = open("name_list", "wb")

pickle.dump(name_list, binary_file)

binary_file.close()