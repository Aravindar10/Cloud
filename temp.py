# app.py
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            temp = float(request.form.get('temperature'))
            unit = request.form.get('unit')
            
            if unit == 'C':
                result = (temp * 9/5) + 32
                result = f"{temp}°C is {result:.2f}°F"
            elif unit == 'F':
                result = (temp - 32) * 5/9
                result = f"{temp}°F is {result:.2f}°C"
        except ValueError:
            result = "Invalid input. Please enter a valid number."

    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Temperature Converter</title>
    </head>
    <body>
        <h1>Temperature Converter</h1>
        <form method="post">
            <label for="temperature">Temperature:</label>
            <input type="text" id="temperature" name="temperature" required>
            <select name="unit">
                <option value="C">Celsius to Fahrenheit</option>
                <option value="F">Fahrenheit to Celsius</option>
            </select>
            <button type="submit">Convert</button>
        </form>
        {% if result %}
            <h2>Result: {{ result }}</h2>
        {% endif %}
    </body>
    </html>
    ''', result=result)

if __name__ == '__main__':
    app.run(debug=True)
