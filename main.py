from direct.showbase.ShowBase import ShowBase
from panda3d.core import *

loadPrcFile(Filename("config/Config.prc"))

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

app = MyApp()
app.run()
quit()
