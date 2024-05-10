from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('prediction_form.html')

@app.route('/predict', methods=['POST'])
def predict():
    material_number = request.form['material_number']
    month_year = request.form['month_year']
    day_of_week = request.form['day_of_week']

    # Now you have the user inputs, you can pass them to your prediction model
    # and generate predictions
    # For T313 Årsta Express 

    # For now, let's just return a simple response to confirm that the form submission was received
    return f"Predictions for Material Number: {material_number}, MonthYear: {month_year}, DayOfWeek: {day_of_week}"

if __name__ == '__main__':
    app.run(debug=True)
