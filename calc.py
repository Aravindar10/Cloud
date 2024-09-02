# app.py
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form.get('num1'))
            num2 = float(request.form.get('num2'))
            operation = request.form.get('operation')
            
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error: Division by zero"
        except ValueError:
            result = "Invalid input. Please enter valid numbers."

    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Calculator</title>
    </head>
    <body>
        <h1>Simple Calculator</h1>
        <form method="post">
            <label for="num1">Number 1:</label>
            <input type="text" id="num1" name="num1" required>
            <br>
            <label for="num2">Number 2:</label>
            <input type="text" id="num2" name="num2" required>
            <br>
            <label for="operation">Operation:</label>
            <select id="operation" name="operation">
                <option value="add">Add</option>
                <option value="subtract">Subtract</option>
                <option value="multiply">Multiply</option>
                <option value="divide">Divide</option>
            </select>
            <br>
            <button type="submit">Calculate</button>
        </form>
        {% if result is not none %}
            <h2>Result: {{ result }}</h2>
        {% endif %}
    </body>
    </html>
    ''', result=result)

if __name__ == '__main__':
    app.run(debug=True)
