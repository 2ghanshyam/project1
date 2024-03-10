from kivymd.app import MDApp
from kivy.lang import Builder


switchs = """
MDSwitch:
    pos_hint: {"center_x": .5, "center_y":.5}
    width:dp(45)
    on_active: app.check(*args)
    
"""
class Test(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        switch = Builder.load_string(switchs)
        return switch

    def check(self,checkbox, value):
        if value:
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"



if __name__=="__main__":
    Test().run()