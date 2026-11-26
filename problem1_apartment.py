class Resident:
    def __init__(self, name, flat, fee, status="Pending"):
        self.name = name
        self.flat = flat
        self.fee = fee
        self.status = status  # "Paid" or "Pending"

    def display(self):
        print(f"{self.name} | Flat {self.flat} | Rs.{self.fee} | {self.status}")


class Society:
    def __init__(self):
        self.residents = []

    def add_resident(self, resident):
        self.residents.append(resident)

    def display_all(self):
        for r in self.residents:
            r.display()


s = Society()
s.add_resident(Resident("Ravi", "A101", 2500, "Paid"))
s.add_resident(Resident("Priya", "B202", 3000, "Pending"))
s.display_all()
