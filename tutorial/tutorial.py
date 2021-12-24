from typing import Text
import kivy
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self,**kwargs):
        # call the grid layout contructor
        super(MyGridLayout,self).__init__(**kwargs)

        # Set columns
        self.cols = 1

        # create a second grid
        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        # add widgets
        self.top_grid.add_widget(Label(text="Name: "))
        # add input box
        self.name = TextInput(multiline=True)
        self.top_grid.add_widget(self.name)

        # add widgets
        self.top_grid.add_widget(Label(text="favorite pizza: "))
        # add input box
        self.pizza = TextInput(multiline=True)
        self.top_grid.add_widget(self.pizza)

        # add widgets
        self.top_grid.add_widget(Label(text="Favorite color: "))
        # add input box
        self.color = TextInput(multiline=True)
        self.top_grid.add_widget(self.color) 

        # add new top grid to our app
        self.add_widget(self.top_grid)

        
        # create a submit button
        self.submit = Button(text="Submit",font_size=32)
        # bind the button
        self.submit.bind(on_press=self.press)

        self.add_widget(self.submit)

    def press(self,instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        
         # add widgets
        self.add_widget(Label(text=f"Hello {name}. You like {pizza} pizza and your favorite color is {color}."))
        
        # clear the input bozes
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""



class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()