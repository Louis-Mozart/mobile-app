import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import requests

class MyBoxLayout(BoxLayout):
    input_value = ObjectProperty(None)
    prediction_label = ObjectProperty(None)

    def predict(self):
        input_value = self.input_value.text
        if input_value:
            response = requests.post('http://127.0.0.1:5000/predict', json={'inputValue': input_value})
            if response.status_code == 200:
                prediction = response.json().get('prediction')
                self.prediction_label.text = f'Prediction: {prediction}'
            else:
                self.prediction_label.text = 'Error in prediction'

class MyApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    MyApp().run()
