from urllib.parse import parse_qs

from flask import Flask, redirect, render_template, request, session
from requests import get, post

app = Flask(__name__)

app.config.from_object('config')


@app.route('/')
def index():
    url = 'https://github.com/login/oauth/authorize'
    client_id = app.config.get('CLIENT_ID')
    github = f'{url}?scope=user:email&client_id={client_id}'
    return render_template('index.html', github=github)


@app.route('/callback')
def callback():
    code = request.args.get('code')

    body = {
        'client_id': app.config.get('CLIENT_ID'),
        'client_secret': app.config.get('CLIENT_SECRET'),
        'code': code
    }

    response = post('https://github.com/login/oauth/access_token', json=body)

    access_token = parse_qs(response.text)['access_token'][0]

    response = get(f'https://api.github.com/user?access_token={access_token}')

    auth_result = response.json()

    session['access_token'] = access_token
    session['name'] = auth_result['name']
    session['avatar'] = auth_result['avatar_url']
    session['bio'] = auth_result['bio']

    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    name = session['name']
    avatar = session['avatar']
    bio = session['bio']

    return render_template('dashboard.html',
                           name=name,
                           avatar=avatar,
                           bio=bio)
