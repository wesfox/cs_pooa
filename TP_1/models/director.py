from employee import Employee

class Director(Employee):
    def __init__(self, name, surname, nb_enfant, date_arrive, tel=None):
        super(name, surname, nb_enfant, date_arrive)

        self.__employe_type = "Director"
        self.__tel = tel
        self.__salaire = Salaire(self.__employe_type)
        self.__conge = Conge(self.__employe_type)
