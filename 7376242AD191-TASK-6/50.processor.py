class Processor:
    def process(self):
        pass

class CPU(Processor):
    def process(self):
        print("CPU Processing")

p = CPU()
p.process()
