import kivy
kivy.require('1.11.1')
from plyer import accelerometer, tts
from kivmob import KivMob, TestIds
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
    ads = KivMob(TestIds.APP)
    ads.new_interstitial(TestIds.INTERSTITIAL)
    ads.request_interstitial()
    ads.show_interstitial()
    moves=[]
    health=100
    enemy_health=100
    ecounter=5
    ucounter=3
    chosen_attack=""
    userA=""
    e_count=None
    u_count=None
    accelerometer.enable()
    print(accelerometer.acceleration)
    def enemy_counter(self):
        print(MenuScreen.ecounter)
        MenuScreen.ecounter-=1
        if MenuScreen.ecounter<=0:
            if MenuScreen.chosen_attack=="Fireball!":
                if MenuScreen.userA=="Shield":
                    tts.speak(message="Defended!")
                    MenuScreen.ecounter=5
                    Clock.unschedule((MenuScreen.e_count))
                    if MenuScreen.enemy_health<=0:
                        print("Game End")
                    else:
                        MenuScreen.eevent = Clock.schedule_interval((MenuScreen.enemy_attack), 3)
                    
                else:
                    MenuScreen.health-=10
                    tts.speak(message=str(MenuScreen.health)+" Health Left")
                    if MenuScreen.health<=0:
                        tts.speak(message="Enemy Wins")
                        MenuScreen.ecounter=5
                        Clock.unschedule((MenuScreen.e_count))
                    else:
                        MenuScreen.ecounter=5
                        Clock.unschedule((MenuScreen.e_count))
                        if MenuScreen.enemy_health<=0:
                            print("Game End")
                        else:
                            MenuScreen.eevent = Clock.schedule_interval((MenuScreen.enemy_attack), 3)
                    

            elif MenuScreen.chosen_attack=="Lightning!":
                if MenuScreen.userA=="Shield":
                    tts.speak(message="Defended!")
                    MenuScreen.ecounter=5
                    Clock.unschedule((MenuScreen.e_count))
                    if MenuScreen.enemy_health<=0:
                        print("Game End")
                    else:
                        MenuScreen.eevent = Clock.schedule_interval((MenuScreen.enemy_attack), 3)
                    
                else:
                    MenuScreen.health-=10
                    tts.speak(message=str(MenuScreen.health)+" Health Left")
                    if MenuScreen.health<=0:
                        tts.speak(message="Enemy Wins")
                        MenuScreen.ecounter=5
                        Clock.unschedule((MenuScreen.e_count))
                    else:
                        MenuScreen.ecounter=5
                        Clock.unschedule((MenuScreen.e_count))
                        if MenuScreen.enemy_health<=0:
                            print("Game End")
                        else:
                            MenuScreen.eevent = Clock.schedule_interval((MenuScreen.enemy_attack), 3)
                    

            elif MenuScreen.chosen_attack=="Energy Blast!":
                if MenuScreen.userA=="Shield":
                    tts.speak(message="Defended!")
                    MenuScreen.ecounter=5
                    Clock.unschedule((MenuScreen.e_count))
                    MenuScreen.eevent = Clock.schedule_interval((MenuScreen.enemy_attack), 3)
                    
                else:
                    MenuScreen.health-=20
                    tts.speak(message=str(MenuScreen.health)+" Health Left")
                    if MenuScreen.health<=0:
                        tts.speak(message="Enemy Wins")
                        MenuScreen.ecounter=5
                        Clock.unschedule((MenuScreen.e_count))
                    else:
                        MenuScreen.ecounter=5
                        Clock.unschedule((MenuScreen.e_count))
                        if MenuScreen.enemy_health<=0:
                            print("Game End")
                        else:
                            MenuScreen.eevent = Clock.schedule_interval((MenuScreen.enemy_attack), 3)
                    

            elif MenuScreen.chosen_attack=="Circle Of Pain!":
                if MenuScreen.userA=="Shield":
                    MenuScreen.health-=5
                else:
                    MenuScreen.health-=30
                tts.speak(message=str(MenuScreen.health)+" Health Left")
                if MenuScreen.health<=0:
                    tts.speak(message="Enemy Wins")
                    MenuScreen.ecounter=5
                    Clock.unschedule((MenuScreen.e_count))
                else:
                    MenuScreen.ecounter=5
                    Clock.unschedule((MenuScreen.e_count))
                    if MenuScreen.enemy_health<=0:
                        print("Game End")
                    else:
                        MenuScreen.eevent = Clock.schedule_interval((MenuScreen.enemy_attack), 3)
            else:
                if MenuScreen.health<=0:
                    tts.speak(message="Enemy Wins")
                    MenuScreen.ecounter=5
                    Clock.unschedule((MenuScreen.e_count))
                else:
                    MenuScreen.ecounter=5
                    Clock.unschedule((MenuScreen.e_count))
                    if MenuScreen.enemy_health<=0:
                        print("Game End")
                    else:
                        MenuScreen.eevent = Clock.schedule_interval((MenuScreen.enemy_attack), 3)
                

    def enemy_attack(self):
        print("good")
        attacks=["Fireball!","Lightning!","Energy Blast!","Circle Of Pain!","Shield"]
        MenuScreen.chosen_attack=random.choice(attacks)
        tts.speak(message="Enemy Used "+ str(MenuScreen.chosen_attack))
        Clock.unschedule(MenuScreen.eevent)
        MenuScreen.e_count = Clock.schedule_interval((MenuScreen.enemy_counter), 1)

    eevent = Clock.schedule_interval((enemy_attack), 3)
    
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
            MenuScreen.userA="Fire"
            tts.speak(message="Fireball!")
            self.moves=[]
            MenuScreen.u_count = Clock.schedule_interval((MenuScreen.user_counter), 1)

        elif self.moves==["l","u","r","u"]:
            MenuScreen.userA="Light"
            tts.speak(message="Lightning!") 
            self.moves=[]
            MenuScreen.u_count = Clock.schedule_interval((MenuScreen.user_counter), 1)

        elif self.moves==["u","l","d","r","u"]:
            MenuScreen.userA="Circle Of Pain"
            tts.speak(message="Circle Of Pain!")
            self.moves=[]
            MenuScreen.u_count = Clock.schedule_interval((MenuScreen.user_counter), 1)

        elif self.moves==["l","r"]:
            MenuScreen.userA="Shield"
            tts.speak(message="Shield!")
            self.moves=[]
            MenuScreen.u_count = Clock.schedule_interval((MenuScreen.user_counter), 1)  
        
    def user_counter(self):
        #tts.speak(message=str(MenuScreen.ucounter))
        print(MenuScreen.ucounter)
        MenuScreen.ucounter-=1
        if MenuScreen.ucounter<=0:
            if MenuScreen.userA=="Fire":
                if MenuScreen.chosen_attack=="Shield":
                    tts.speak(message="Enemy Defended!")
                    MenuScreen.ucounter=3
                    Clock.unschedule((MenuScreen.u_count))

                else:
                    MenuScreen.enemy_health-=10
                    tts.speak(message=str(MenuScreen.enemy_health)+" Enemy Health Left")
                    if MenuScreen.enemy_health<=0:
                        tts.speak(message="You Win!")
                    
                    MenuScreen.ucounter=3
                    Clock.unschedule((MenuScreen.u_count))

            elif MenuScreen.userA=="Light":
                if MenuScreen.chosen_attack=="Shield":
                    tts.speak(message="Enemy Defended!")
                    MenuScreen.ucounter=3
                    Clock.unschedule((MenuScreen.u_count))
                else:
                    MenuScreen.enemy_health-=10
                    tts.speak(message=str(MenuScreen.enemy_health)+" Enemy Health Left")
                    if MenuScreen.enemy_health<=0:
                        tts.speak(message="You Win!")
                    
                    MenuScreen.ucounter=3
                    Clock.unschedule((MenuScreen.u_count))


            elif MenuScreen.userA=="Circle Of Pain":
                if MenuScreen.chosen_attack=="Shield":
                    MenuScreen.enemy_health-=5
                else:
                    MenuScreen.enemy_health-=30
                tts.speak(message=str(MenuScreen.enemy_health)+" Enemy Health Left")
                if MenuScreen.enemy_health<=0:
                    tts.speak(message="You Win!")

                MenuScreen.ucounter=3
                Clock.unschedule(MenuScreen.u_count)
            else:
                MenuScreen.ucounter=3
                Clock.unschedule(MenuScreen.u_count)
                    
            
    

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

