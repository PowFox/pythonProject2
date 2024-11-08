class Achievement: ...

class Employee:
    def __init__(self, vardas: str, pavarde: str, salary: int, achievements: list[Achievement]):
        self.vardas = vardas
        self.pavarde = pavarde
        self.salary = salary
        self.achievements = achievements

    def calc_post_tax(self):
        return self.salary * 0.61

    def get_fullname(self):
        return f"{self.vardas} {self.pavarde}"

    def __repr__(self):
        return f"| {self.vardas} {self.pavarde} - {self.salary} |"

    def __str__(self):
        """This is a simple change"""
        return self.__repr__()