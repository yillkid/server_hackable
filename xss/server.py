import requests
import json
from flask import Flask, request, render_template
from flask_login import login_user, LoginManager, \
        UserMixin, login_required, current_user, logout_user
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/s1', methods=['GET', 'POST'])
def s1():
    
    if request.method == 'POST':
        data = request.form;
        return render_template('s1.html', result = data["p1"])

    return render_template('s1.html')


@app.route('/s2', methods=['GET', 'POST'])
def s2():
    
    if request.method == 'POST':
        data = request.form;
        return render_template('s2.html', result = data["p1"])

    return render_template('s2.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8886, debug=True)
