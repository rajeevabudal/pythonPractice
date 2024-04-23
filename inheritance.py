class Employee:
    def __init__(self, name):
        self.name = name;


class Dance:
    def __init__(self, danceStyle):
        self.danceStyle = danceStyle


class dancerEmployee(Dance, Employee):
    def __init__(self, danceStyle, name):
        self.danceStyle = danceStyle
        self.name = name

o = dancerEmployee("BharathaNatyam", "rajeeva")
print(o.name, o.danceStyle)