from typing import Text
import kivy
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGridLayout(GridLayout):
    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        
         # add widgets
        # self.add_widget(Label(text=f"Hello {name}. You like {pizza} pizza and your favorite color is {color}."))
        print(f"Hello {name}. You like {pizza} pizza and your favorite color is {color}.")
        # clear the input bozes
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""



class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()