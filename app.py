from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    participants = request.form.get('participants', '')
    hourly_rate = request.form.get('hourly_rate', '')
    meeting_length = request.form.get('meeting_length', '')
    result = None

    if request.method == 'POST':
        if 'calculate' in request.form:
            try:
                participants = int(participants)
                hourly_rate = int(hourly_rate)
                meeting_length = int(meeting_length)
                result = (participants * hourly_rate * meeting_length) / 60
            except ValueError:
                result = None

    return render_template('calculator.html', 
                           participants=participants, 
                           hourly_rate=hourly_rate, 
                           meeting_length=meeting_length, 
                           result=result)

if __name__ == '__main__':
    app.run(debug=True)