class stud:
    __id=1
    __nm="riya"

    def __get(self):
        print(self.__id)
        print(self.__nm)
    def show(self):
        self.__get()

s=stud()
s.show()