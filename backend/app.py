from flask import Flask, request, jsonify, render_template
from model import predict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_route():
    # Check if the data is coming from a form submission
    if request.content_type == 'application/x-www-form-urlencoded':
        age = int(request.form['age'])
        gender = request.form['gender']
    # Otherwise, assume it's JSON data
    else:
        data = request.get_json()
        age = data.get('age')
        gender = data.get('gender')

    prediction = predict(age, gender)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
