class Employee:
    def __init__(self, vardas, pavarde, salary):
        self.vardas = vardas
        self.pavarde = pavarde
        self.salary = salary

    def __repr__(self):
        return f"| {self.vardas} {self.pavarde} - {self.salary} |"
