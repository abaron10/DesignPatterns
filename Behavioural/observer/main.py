from DataSource import DataSource
from Chart import Chart
from SpreadSheet import SpreadSheet

#Observer
# es un patrón de diseño de software que define una dependencia del tipo uno a muchos entre objetos, 
# de manera que cuando uno de los objetos cambia su estado, notifica este cambio a todos los dependientes

if __name__ == '__main__':
    data = DataSource()
    sheet1 = SpreadSheet()
    sheet2 = SpreadSheet()
    chart = Chart()

    data.addObserver(sheet1)
    data.addObserver(sheet2)
    data.addObserver(chart)

    data.setValue(1)
