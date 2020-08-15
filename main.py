import kivy
kivy.require('1.11.1')
from plyer import accelerometer, tts

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
        counter=0
        accelerometer.enable()
        while counter<100:
            if float(accelerometer.acceleration)[0]> 8.0:
                tts.speak(message="Forward")
                counter+=1
            elif float(accelerometer.acceleration)[0]< -8.0:
                tts.speak(message="Backward")
                counter+=1
            elif float(accelerometer.acceleration)[1]> 8.0:
                tts.speak(message="Up")
            elif float(accelerometer.acceleration)[1]< -8.0:
                tts.speak(message="Down")
            elif float(accelerometer.acceleration)[2]> 8.0:
                tts.speak(message="Left")
            elif accelerometer.acceleration[2]< -8.0:
                tts.speak(message="Right")

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

