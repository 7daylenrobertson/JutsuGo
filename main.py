import kivy
kivy.require('1.11.1')
from plyer import gyroscope, vibrator

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.clock import Clock

Builder.load_string("""
#:import facade plyer.gyroscope

<MenuScreen>:
    facade:facade
    start:start
    stop:stop

    FloatLayout:
        Button:
            id:start
            disabled: False
            background_color: 0,1,0,1
            text:"Click to start sensor"
            pos_hint:{"x":0.2,"y":0.3}
            size_hint: 0.3 , 0.3
            on_release:
                root.enable()
                stop.disabled = not stop.disabled
                start.disabled = not start.disabled
        
        Button:
            id:stop
            disabled: True
            background_color: 1,0,0,1
            text:"Click to stop sensor"
            pos_hint:{"x":0.6,"y":0.3}
            size_hint: 0.3 , 0.3
            on_release:
                root.disable()
                vibrator.vibrate(1)
                stop.disabled = not stop.disabled
                start.disabled = not start.disabled
        
        Label:
            background_color:1,1,1,1
            text:str(root.gyrotext)
            halign: 'center'
            valign: 'center'
            font_size: 10
            pos_hint:{"x":0.5,"y":0.7}


""")


class MenuScreen(Screen):
    gyrotext=NumericProperty(0)  
    facade=ObjectProperty()

    def enable(self):
        self.facade.enable()
        Clock.schedule_interval(self.get_rotation,1/20.)
        Clock.schedule_interval(self.get_rotation_uncalib,1/20.)
        print("Gyro is being turned on")
        vibrator.vibrate(1)
    
    def disable(self):
        self.facade.disable()
        Clock.unschedule(self.get_rotation)
        Clock.unschedule(self.get_rotation_uncalib)
        print("Gyro is being turned off")   

    def get_rotation(self, dt):
        if self.facade.rotation != (None, None, None):
            print("NORMAL:",self.facade.rotation)
            
    def get_rotation_uncalib(self, dt):
        empty = tuple([None for i in range(6)])

        if self.facade.rotation_uncalib != empty:
            self.gyrotext=self.facade.rotation_uncalib
            print("UNCALIB:",self.facade.rotation_uncalib)

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

