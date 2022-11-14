def generarPares(limite):
    num = 1

    while num < limite:
        
        yield num*2

        num = num+1

devuelvePares = generarPares(10)

print(next(devuelvePares))
print("Aqui podría ir mas codigo")

print(next(devuelvePares))
print("Aqui podría ir mas codigo")

print(next(devuelvePares))
print("Aqui podría ir mas codigo")