class Plugin:
    def run(self):
        pass

class PluginA(Plugin):
    def run(self):
        print("Plugin A Running")

p = PluginA()
p.run()
