from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/customer')
def customer():
    return render_template('customer.html')

@app.route('/sales')
def sales():
    return render_template('sales.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/total_sales')
def total_sales():
    return render_template('total_sales.html')

if __name__ == '__main__':
    app.run()
