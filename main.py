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
            size_hint: 0.2 , 0.2
            on_release:
                root.enable()
        Button:
            background_color: 0,1,0,1
            text:"Click to submit"
            pos_hint:{"x":0.2,"y":0.8}
            size_hint: 0.2 , 0.2
            on_release:
                root.submit()
        
        Button:
            id:stop
            background_color: 1,0,0,1
            text:"Click to stop sensor"
            pos_hint:{"x":0.6,"y":0.3}
            size_hint: 0.2 , 0.2
            on_release:
                root.disable()


""")


class MenuScreen(Screen):
    moves=[]
    def enable(self):
        print("turned on")
        accelerometer.enable()
        try:
            if accelerometer.acceleration[0]> 8.0:
                tts.speak(message="Forward")
                self.moves.append("f")
                print(self.moves)
            elif accelerometer.acceleration[0]< -8.0:
                tts.speak(message="Backward")
                self.moves.append("b")
                print(self.moves)
            elif accelerometer.acceleration[1]> 8.0:
                tts.speak(message="Up")
                self.moves.append("u")
                print(self.moves)
            elif accelerometer.acceleration[1]< -8.0:
                tts.speak(message="Down")
                self.moves.append("d")
                print(self.moves)
            elif accelerometer.acceleration[2]> 8.0:
                tts.speak(message="Right")
                self.moves.append("r")
                print(self.moves)
            elif accelerometer.acceleration[2]< -8.0:
                tts.speak(message="Left")
                self.moves.append("l")
                print(self.moves)
        except:
            print("wait bruh")

    def disable(self):
        self.moves=[]
        tts.speak(message="Retarted!")
        print(self.moves) 

    def submit(self):
        if self.moves==["f","b","f"]:
            tts.speak(message="Fireball!")
            self.moves=[]

        elif self.moves==["l","u","r","u"]:
            tts.speak(message="Lightning!") 
            self.moves=[]

        elif self.moves==["u","l","d","r","u"]:
            tts.speak(message="Circle Of Pain!")
            self.moves=[]  
            
    

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

