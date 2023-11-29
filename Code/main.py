from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

class FirstScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_line = BoxLayout(orientation='vertical', spacing = 8, padding = 8)
        go = Label(text='Hello world!')
        self.btn = Button(text='Again..',size_hint=(.3, .3), pos_hint={'center_x': .5})
        self.btn2 = Button(text='Exit',size_hint=(.2, .2), pos_hint={'center_x': .9})
        
        self.main_line.add_widget(self.btn2)
        self.main_line.add_widget(go)
        self.main_line.add_widget(self.btn)
        
        self.add_widget(self.main_line)

        self.btn.on_press = self.next2
        self.btn2.on_press = self.next
    def next(self):
        App().get_running_app().stop()
    def next2(self):
        self.manager.current = 'second'

class SecondScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_line = BoxLayout(orientation='vertical', padding=8, spacing=8)
        go = Label(text='Yes. What the problem?', halign='center')
        self.btn = Button(text='Nothing. Sorry.', size_hint=(.2,.3), pos_hint={'center_x':.5})
        self.btn2 = Button(text='This text is boring.', size_hint=(.2,.3), pos_hint={'center_x':.5})
        self.btn3 = Button(text='Exit',size_hint=(.2, .2), pos_hint={'center_x': .9})
        
        self.main_line.add_widget(self.btn3)
        self.main_line.add_widget(go)
        self.main_line.add_widget(self.btn)
        self.main_line.add_widget(self.btn2)
        
        self.add_widget(self.main_line)
        
        self.btn3.on_press = self.exit
        self.btn.on_press = self.next
        self.btn2.on_press = self.next2
        
    def exit(self):
        App().get_running_app().stop()
    def next(self):
        self.manager.current = 'third'
    def next2(self):
        self.manager.current = 'fourth'
        
class ThirdScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_line = BoxLayout(orientation='vertical', padding=8, spacing=8)
        go = Label(text='It is okay, brother. Just relax. You can leave this application or retreat=)')
        self.btn = Button(text='Exit', size_hint=(.2, .2), pos_hint={'center_x': .9})
        self.btn2 = Button(text='Retreat', size_hint=(.2, .3), pos_hint={'center_x': .5})
        
        self.main_line.add_widget(self.btn)
        self.main_line.add_widget(go)
        self.main_line.add_widget(self.btn2)
        
        self.add_widget(self.main_line)
        
        self.btn.on_press = self.exit
        self.btn2.on_press = self.next

    def exit(self):
        App().get_running_app().stop()
    def next(self):
        self.manager.current = 'second'
        
class FourthScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_line = BoxLayout(orientation='vertical', padding=8, spacing=8)
        go = Label(text='Goodbye, traitor.')
        self.btn = Button(text='Exit', size_hint=(.2, .2), pos_hint={'center_x': .5})
         
        self.main_line.add_widget(go)
        self.main_line.add_widget(self.btn)
        
        self.add_widget(self.main_line)
        
        self.btn.on_press = self.exit

    def exit(self):
        App().get_running_app().stop()
        
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr(name='first'))
        sm.add_widget(SecondScr(name='second'))
        sm.add_widget(ThirdScr(name='third'))
        sm.add_widget(FourthScr(name='fourth'))

        return sm
    
MyApp().run()