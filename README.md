<p align="center">
  <img src="https://user-images.githubusercontent.com/17479978/63855278-6be46e80-c975-11e9-9fb2-77a5d5f79814.png" width="75%">
</p>

<h1 align="center">Payment Iugu</h1>

## Usage

### Run local

1. Clone the repository.
```shell
git clone https://github.com/flaviogf/payment_iugu.git
```
2. Create virtual env.
```shell
python3.7 -m venv venv
```
3. Install dependencies.
```shell
pip install pipenv && pipenv install -d
```
3. Set variables on settings.ini.
```
CLIENT_ID=YOUR_CLIENT_ID
CLIENT_SECRET=YOUR_CLIENT_SECRET
SECRET_KEY=YOUR_SECRET_KEY
ACCOUNT_ID=YOUR_ACCOUNT_ID
```
4. Run application.
```shell
FLASK_APP=app.py FLASK_ENV=development FLASK_DEBUG=1 flask run
```
