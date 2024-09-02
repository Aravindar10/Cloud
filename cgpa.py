# app.py
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    cgpa = None
    if request.method == 'POST':
        try:
            grades = request.form.getlist('grade')
            credits = request.form.getlist('credit')
            
            total_points = 0
            total_credits = 0

            for grade, credit in zip(grades, credits):
                grade = float(grade)
                credit = float(credit)
                total_points += grade * credit
                total_credits += credit

            if total_credits != 0:
                cgpa = total_points / total_credits
            else:
                cgpa = "Error: Total credits cannot be zero."
        except ValueError:
            cgpa = "Invalid input. Please enter valid numbers."

    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>CGPA Calculator</title>
    </head>
    <body>
        <h1>CGPA Calculator</h1>
        <form method="post">
            <div id="courses">
                <div>
                    <label for="grade1">Grade:</label>
                    <input type="text" id="grade1" name="grade" required>
                    <label for="credit1">Credit Hours:</label>
                    <input type="text" id="credit1" name="credit" required>
                </div>
            </div>
            <button type="button" onclick="addCourse()">Add More Courses</button>
            <br>
            <button type="submit">Calculate CGPA</button>
        </form>
        {% if cgpa is not none %}
            <h2>CGPA: {{ cgpa }}</h2>
        {% endif %}
        <script>
            let courseCount = 1;
            function addCourse() {
                courseCount++;
                const courseDiv = document.createElement('div');
                courseDiv.innerHTML = `
                    <label for="grade${courseCount}">Grade:</label>
                    <input type="text" id="grade${courseCount}" name="grade" required>
                    <label for="credit${courseCount}">Credit Hours:</label>
                    <input type="text" id="credit${courseCount}" name="credit" required>
                `;
                document.getElementById('courses').appendChild(courseDiv);
            }
        </script>
    </body>
    </html>
    ''', cgpa=cgpa)

if __name__ == '__main__':
    app.run(debug=True)
