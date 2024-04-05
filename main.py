from flask import Flask, request, jsonify, session, url_for, redirect
from flask_cors import CORS

from core.spark import create_deck, submit_game, login, get_decks, query_user
from views import views

import smtplib

from email.mime.text import MIMEText

app = Flask(__name__)
app.register_blueprint(views, url_prefix='/')
app.secret_key = 'spark-key'
CORS(app)


@app.route('/api/login', methods=['POST'])
def server_login():
  if request.is_json:
    data = request.json
    response = login(data)
    session['username'] = data.get('username')
    session['user_id'] = response['user_id']
    return jsonify(response), 200


@app.route('/api/logout', methods=['POST'])
def server_logout():
  if request and 'user_id' in session:
    del session['user_id']
    response = {
        'status': 'success',
        'message': 'user was successfully logged out'
    }
    return jsonify(response), 200


@app.route('/api/deck', methods=['PUT', 'POST'])
def server_submit_deck():
  if request.is_json and 'user_id' in session:
    data = request.json
    user_id = session['user_id']
    response = create_deck(data, user_id)
    return jsonify(response), 200


@app.route('/api/game', methods=['POST'])
def server_submit_game():
  if request.is_json and 'user_id' in session:
    data = request.json
    user_id = session['user_id']
    response = submit_game(data, user_id)
    if (response['status'] == 'error'):
      return jsonify(response), 400
    return jsonify(response), 200


@app.route('/api/users/', methods=['GET'])
def server_get_users():
  if request and request.args.get('search'):
    username_query = request.args.get('search')
    response = query_user(username_query)
    if (response['status'] == 'error'):
      return jsonify(response), 400
    return jsonify(response), 200


@app.route('/api/deck', methods=['GET'])
def server_get_deck():
  if request.headers:
    session_id = request.headers
    response = get_decks(session_id)
    return jsonify(response), 200


@app.route('/send', methods=['GET'])
def send_email():
  contents = 'hello Martin, this is a test'

  msg = MIMEText(contents)

  msg['Subject'] = 'This is the test'
  msg['From'] = 'martin.liriano@gmail.com'
  msg['To'] = ', '.join('sprite599@gmail.com')

  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
    smtp_server.login('martin.liriano@gmail.com', 'ccez ekei usjr egmv')
    smtp_server.sendmail('martin.liriano@gmail.com', 'sprite599@gmail.com',
                         msg.as_string())


if __name__ == '__main__':
  app.run(debug=True, port=8000)
