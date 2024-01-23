# This will require KivyMD to run in Android.

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from datetime import datetime

class DigitalClockWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(DigitalClockWidget, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.time_label = label = Label(font_size=40, halign='center', valign='middle')
        self.add_widget(self.time_label)

        # We want to refresh the method or the function to update in every second.
        Clock.schedule_interval(self.update,1)

    # define the function for update every second
    def update(self, dt):
        current_time = datetime.now().strftime('%H:%M:%S')
        self.time_label.text = current_time    

class DigitalClockApp(App):
    def build(self):
        return DigitalClockWidget()


if __name__ == 'main':
    DigitalClockApp().run()    