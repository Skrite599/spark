from flask import Flask, request, jsonify, session
from flask_cors import CORS

from core.spark import create_deck, submit_game, login, query_user, create_user, process_cards, process_combos
from views import views
from util.parser import parse_deck

import smtplib
import ssl
from email.message import EmailMessage

# app = Flask(__name__)
# app.register_blueprint(views, url_prefix='/')
# app.secret_key = 'spark-key'
# CORS(app)


# @app.route('/api/login', methods=['POST'])
# def server_login():
#   if request.is_json:
#     data = request.json
#     response = login(data)
    
#     if response['message'] == 'user does not exist' :
#       return jsonify(response), 400
    
#     session['username'] = data.get('username')
#     session['user_id'] = response['user_id']
#     return jsonify(response), 200
#   else:
#     response = {
#       'status': 'error',
#       'message': 'incorrect request was sent'
#     }
#     return jsonify(response), 400
  
  
# @app.route('/api/signup', methods=['POST'])
# def server_signup():
#   if request.is_json and 'username' not in session:
#     data = request.json
#     response = create_user(data)
#     if response['status'] != 'success':
#       return jsonify(response), 400
#     session['user_id'] = response['user_id']
#     session['username'] = response['username']
#     return jsonify(response), 200
#   else:
#     response = {
#       'status': 'error',
#       'message': 'incorrect request was sent'
#     }
#     return jsonify(response), 400


# @app.route('/api/logout', methods=['POST'])
# def server_logout():
#   if request and 'user_id' in session and 'username' in session:
#     del session['user_id']
#     del session['username']
#     response = {
#         'status': 'success',
#         'message': 'user was successfully logged out'
#     }
#     return jsonify(response), 200
#   else:
#     response = {
#       'status': 'error',
#       'message': 'incorrect request was sent'
#     }
#     return jsonify(response), 400


# @app.route('/api/deck', methods=['PUT', 'POST'])
# def server_submit_deck():
#   if request.is_json and 'user_id' in session:
#     data = request.json
#     user_id = session['user_id']
#     response = create_deck(data, user_id)
#     return jsonify(response), 200
#   else:
#     response = {
#       'status': 'error',
#       'message': 'incorrect request was sent'
#     }
#     return jsonify(response), 400


# @app.route('/api/game', methods=['POST'])
# def server_submit_game():
#   if request.is_json and 'user_id' in session:
#     data = request.json
#     user_id = session['user_id']
#     response = submit_game(data, user_id)
#     if (response['status'] == 'error'):
#       return jsonify(response), 400
#     return jsonify(response), 200
#   else:
#     response = {
#       'status': 'error',
#       'message': 'incorrect request was sent'
#     }
#     return jsonify(response), 400


# @app.route('/api/users/', methods=['GET'])
# def server_get_users():
#   if request and request.args.get('search'):
#     username_query = request.args.get('search')
#     response = query_user(username_query)
#     if (response['status'] == 'error'):
#       return jsonify(response), 400
#     return jsonify(response), 200
#   else:
#     response = {
#       'status': 'error',
#       'message': 'incorrect request was sent'
#     }
#     return jsonify(response), 400

# @app.route('/send', methods=['GET'])
# def send_email():
#   contents = 'hello Martin, this is a test'
#   password = 'gkmglznsfupaxgrn'

#   msg = EmailMessage()

#   msg['Subject'] = 'This is the test'
#   msg['From'] = 'martin.liriano@gmail.com'
#   msg['To'] = 'sprite599@gmail.com'
#   msg.set_content(contents)

#   # Add SSL (layer of security)
#   context = ssl.create_default_context()

#   # Log in and send the email
#   with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#     smtp.login('martin.liriano@gmail.com', password)
#     smtp.sendmail('martin.liriano@gmail.com', 'sprite599@gmail.com', msg.as_string())
#   return 200



# if __name__ == '__main__':
#   app.run(debug=True, port=8000)

process_combos()