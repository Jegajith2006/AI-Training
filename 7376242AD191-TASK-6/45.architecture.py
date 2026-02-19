class Engine:
    def run(self):
        pass

class Module(Engine):
    def run(self):
        print("Module Running")

m = Module()
m.run()
