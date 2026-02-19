class Report:
    def generate(self):
        pass

class SalesReport(Report):
    def generate(self):
        print("Sales Report Generated")

r = SalesReport()
r.generate()
