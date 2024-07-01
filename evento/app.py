from flask import Flask, render_template, url_for # type: ignore

app = Flask(__name__)

# Sample data
pricing_data = [
    {'id': 1, 'name': 'Basic Plan', 'price': '$99', 'full_service': 'Yes', 'decoration': 'Yes', 'music_photo': 'Yes', 'food_drinks': 'Yes', 'invitation_card': 'Yes'},
    {'id': 2, 'name': 'Standard Plan', 'price': '$199', 'full_service': 'Yes', 'decoration': 'Yes', 'music_photo': 'Yes', 'food_drinks': 'Yes', 'invitation_card': 'Yes'},
    # Add more plans as needed
]

@app.route('/')
def pricing():
    return render_template('price.html', data=pricing_data)

@app.route('/details/<int:plan_id>')
def view_details(plan_id):
    plan = next((item for item in pricing_data if item["id"] == plan_id), None)
    if plan is None:
        return "Plan not found", 404
    return render_template('View_details.html', pricing_plan=plan)

if __name__ == '__main__':
    app.run(debug=True)
