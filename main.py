import kivy
kivy.require('1.11.1')
from plyer import accelerometer, tts

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.clock import Clock
import random
from functools import partial

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
    health=100
    enemy_health=100
    ecounter=3
    ucounter=3
    chosen_attack=""
    userA=""
    accelerometer.enable()
    print(accelerometer.acceleration)
    def enemy_counter(self):
        print("hey 2")
        tts.speak(message=str(MenuScreen.ecounter))
        MenuScreen.ecounter-=1
        if MenuScreen.ecounter<=0:
            if MenuScreen.chosen_attack=="Fireball!":
                if MenuScreen.userA=="Shield":
                    tts.speak(message="Defended!")
                    MenuScreen.ecounter=3
                    Clock.unschedule((MenuScreen.e_count))
                    eevent = Clock.schedule_interval(MenuScreen.enemy_attack, 3)
                    
                else:
                    MenuScreen.health-=10
                    tts.speak(message=str(MenuScreen.health)+" Health Left")
                    MenuScreen.ecounter=3
                    Clock.unschedule((MenuScreen.e_count))
                    eevent = Clock.schedule_interval(MenuScreen.enemy_attack, 3)
                    

            elif MenuScreen.chosen_attack=="Lightning!":
                if MenuScreen.userA=="Shield":
                    tts.speak(message="Defended!")
                    MenuScreen.ecounter=3
                    Clock.unschedule((MenuScreen.e_count))
                    eevent = Clock.schedule_interval(MenuScreen.enemy_attack, 3)
                    
                else:
                    MenuScreen.health-=10
                    tts.speak(message=str(MenuScreen.health)+" Health Left")
                    MenuScreen.ecounter=3
                    Clock.unschedule((MenuScreen.e_count))
                    eevent = Clock.schedule_interval(MenuScreen.enemy_attack, 3)
                    

            elif MenuScreen.chosen_attack=="Energy Blast!":
                if MenuScreen.userA=="Shield":
                    tts.speak(message="Defended!")
                    MenuScreen.ecounter=3
                    Clock.unschedule((MenuScreen.e_count))
                    eevent = Clock.schedule_interval(MenuScreen.enemy_attack, 3)
                    
                else:
                    MenuScreen.health-=20
                    tts.speak(message=str(MenuScreen.health)+" Health Left")
                    MenuScreen.ecounter=3
                    Clock.unschedule((MenuScreen.e_count))
                    eevent = Clock.schedule_interval(MenuScreen.enemy_attack, 3)
                    

            elif MenuScreen.chosen_attack=="Circle Of Pain!":
                if MenuScreen.userA=="Shield":
                    MenuScreen.health-=5
                else:
                    MenuScreen.health-=30
                tts.speak(message=str(MenuScreen.health)+" Health Left")
                MenuScreen.ecounter=3
                Clock.unschedule((MenuScreen.e_count))
                eevent = Clock.schedule_interval(MenuScreen.enemy_attack, 3)
                

    def enemy_attack(self):
        print("good")
        attacks=["Fireball!","Lightning!","Energy Blast!","Circle Of Pain!","Shield"]
        MenuScreen.chosen_attack=random.choice(attacks)
        tts.speak(message=MenuScreen.chosen_attack)
        Clock.unschedule(MenuScreen.eevent)
        e_count = Clock.schedule_interval((MenuScreen.enemy_counter), 1)

    eevent = Clock.schedule_interval((enemy_attack), 3)
    #Clock.unschedule(eevent)
    
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
        tts.speak(message="Restarted!")
        print(self.moves) 

    

    def submit(self):
        if self.moves==["f","b","f"]:
            userA="Fire"
            tts.speak(message="Fireball!")
            self.moves=[]
            u_count = Clock.schedule_interval((MenuScreen.user_counter), 1)

        elif self.moves==["l","u","r","u"]:
            userA="Light"
            tts.speak(message="Lightning!") 
            self.moves=[]
            u_count = Clock.schedule_interval((MenuScreen.user_counter), 1)

        elif self.moves==["u","l","d","r","u"]:
            userA="Circle Of Pain"
            tts.speak(message="Circle Of Pain!")
            self.moves=[]
            u_count = Clock.schedule_interval((MenuScreen.user_counter), 1)

        elif self.moves==["l","r"]:
            userA="Shield"
            tts.speak(message="Shield!")
            self.moves=[]
            u_count = Clock.schedule_interval((MenuScreen.user_counter), 1)  
        
    def user_counter(self):
        print("Yessir")
        tts.speak(message=str(MenuScreen.ucounter))
        MenuScreen.ucounter-=1
        if MenuScreen.ucounter<=0:
            if MenuScreen.userA=="Fire":
                if MenuScreen.chosen_attack=="Shield":
                    tts.speak(message="Enemy Defended!")
                    MenuScreen.ucounter=3
                    Clock.unschedule(u_count)

                else:
                    self.enemy_health-=10
                    tts.speak(message=str(self.enemy_health)+" Enemy Health Left")
                    self.ucounter=3
                    Clock.unschedule(u_count)

            elif self.userA=="Light":
                if self.chosen_attack=="Shield":
                    tts.speak(message="Enemy Defended!")
                    self.ucounter=3
                    Clock.unschedule(u_count)
                else:
                    self.enemy_health-=10
                    tts.speak(message=str(self.enemy_health)+" Enemy Health Left")
                    self.ucounter=3
                    Clock.unschedule(u_count)


            elif self.userA=="Circle Of Pain":
                if self.chosen_attack=="Shield":
                    self.enemy_health-=5
                else:
                    self.enemy_health-=30
                tts.speak(message=str(self.enemy_health)+" Enemy Health Left")
                self.ucounter=3
                Clock.unschedule(u_count)
            
    

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

