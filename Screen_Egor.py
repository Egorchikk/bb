from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.video import Video

class Screen_Egor(Screen):
    def __init__(self, name = 'Egor'):
        super().__init__(name=name)
        txt = Label(text = 'Здарова Хлопцы,' '\n' 'my name is Egor and you have already known it!' '\n' 'Занимаюсь волейболом и эндуро-мотокроссом, учусь в школе 1557 в "Предпрофессиональный IT класс".' '\n' 'Дальше будут кнопочки можете пожмякать <З', size_hint = (1, 1), font_size = (15))
        box = BoxLayout(orientation = 'vertical')
        btn = Button(text = 'ТЫК', size_hint = (0 , 0.5))
        btn.on_press = self.next

        box.add_widget(txt)
        box.add_widget(btn)
        self.add_widget(box)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'Egor1'





class Screen_Egor1(Screen):
    def __init__(self, name = 'Egor1'):
        super().__init__(name=name)

        pic = Image(source = "PIC1.jpg", size_hint = (1, 1))
        pic2 = Image(source = "PIC2.jpg", size_hint = (1, 1))
        pic3 = Image(source = "PIC3.jpg", size_hint = (1, 1))
        box = BoxLayout(orientation = 'horizontal')
        box2 = BoxLayout(orientation = 'vertical')

        btn = Button(text = 'ТЫК Х2', size_hint = (0 , 0))
        btn.on_press = self.next

        box.add_widget(pic)
        box2.add_widget(btn)
        box.add_widget(pic2)
        box.add_widget(pic3)
        self.add_widget(box)
        self.add_widget(box2)

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'Egor2'


class Screen_Egor2(Screen):
    def __init__(self, name = 'Egor2'):
        super().__init__(name=name)
        box = BoxLayout(orientation = 'horizontal')
        video = Video(source='Egorik.avi')

        self.add_widget(box)
        box.add_widget(video)
         









class Main(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Screen_Egor())
        sm.add_widget(Screen_Egor1())
        sm.add_widget(Screen_Egor2())
        return sm

Window.clearcolor = (0, 0, 0, 1)
app = Main()
app.run()