from flask import Flask, request, jsonify, session, url_for, redirect
from flask_cors import CORS

from core.spark import create_deck, submit_game, login, get_decks
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix='/')
app.secret_key = 'spark-key'
CORS(app)


@app.route('/api/login', methods=['POST'])
def server_login():
  if request.form:
    data = request.form
    response = login(data)
    if response:
      session['username'] = data.get('username')
      session['user_id'] = response['user_id']
      return redirect(url_for('views.index'))


@app.route('/api/deck', methods=['PUT', 'POST'])
def server_submit_deck():
  if request.form and 'user_id' in session:
    data = request
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



@app.route('/api/deck', methods=['GET'])
def server_get_deck():
  if request.headers:
    session_id = request.headers
    response = get_decks(session_id)
    return jsonify(response), 200


if __name__ == '__main__':
  app.run(debug=True, port=8000)
