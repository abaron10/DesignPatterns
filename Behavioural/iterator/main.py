from BrowseHIstory import BrowseHistory


if __name__ == '__main__':
    history = BrowseHistory();
    #si queremos iterar sobre estas urls no es posible porque el campo url es privado
    #puedo crear getters y setters pero el problema e ssi cambio la estructura de datos se pueden romper algunas
    #partes. Arraylist / S tack
    history.push("a")
    history.push("b")
    history.push("c")

    itera = iter(history)

    for item in itera:
        print(item)

   