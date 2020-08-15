import kivy
kivy.require('1.11.1')
from plyer import accelerometer

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.clock import Clock

Builder.load_string("""

<MenuScreen>:
    

    FloatLayout:
    
        Button:
            id:start
            background_color: 0,1,0,1
            text:"Click to start sensor"
            pos_hint:{"x":0.2,"y":0.3}
            size_hint: 0.3 , 0.3
            on_release:
                root.enable()
        
        Button:
            id:stop
            background_color: 1,0,0,1
            text:"Click to stop sensor"
            pos_hint:{"x":0.6,"y":0.3}
            size_hint: 0.3 , 0.3
            on_release:
                root.disable()


""")


class MenuScreen(Screen):

    def enable(self):
        print("turned on")
        accelerometer.enable()
        print(accelerometer.acceleration)
    def disable(self):
        accelerometer.disable()
        print("turned OFF")   
            
    

sm=ScreenManager()
sm.add_widget(MenuScreen(name="menu"))
sm.current= "menu"

class MainApp(App):

    def build (self):
        self.title="JutsuGO!"
        return sm 



if __name__=="__main__":
    app=MainApp()
    app.run()

