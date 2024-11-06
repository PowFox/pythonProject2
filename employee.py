class Employee:
    def __init__(self, vardas: str, pavarde: str, salary: int):
        self.vardas = vardas
        self.pavarde = pavarde
        self.salary = salary

    def get_fullname(self):
        return f"{self.vardas} {self.pavarde}"

    def __repr__(self):
        return f"| {self.vardas} {self.pavarde} - {self.salary} |"

    def __str__(self):
        return self.__repr__()
