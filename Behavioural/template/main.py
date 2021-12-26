from TransferMoneyTask import TransferMoneyTask


#Template Pattern
#Permite definir una plantilla (skeleto) mediante una clase abstracta para operaciones. 
#Los steps requeridos para estas operaciones son implementados en subclases.


if __name__ == '__main__':
    task = TransferMoneyTask()
    task.execute()    