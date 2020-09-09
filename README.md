# Education Loan


This project consists in registering a user and checking some of it's data.
The main idea of the architecture was based on the Clean Architecture, so I chose to follow the Hexagonal Architecture.

 - It was only tested on Linux.
 

## Requirements

 - Make
 - Python 3.8+
 - pyenv


## Development Environment
 
 
### Automation tool

This project uses `Makefile` as automation tool. Replace `edu-loan` label to your project name.

### Set-up Virtual Environment

The following commands will install and set-up `pyenv` tool (https://github.com/pyenv/pyenv) used to create/manage virtual environments:

> Just replace `zshrc` with the configuration file of your interpreter, like `bashrc`

```bash
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.zshrc
$ exec "$SHELL"
$ git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
$ exec "$SHELL"
```

After that, access the project directory and execute `make create-venv` to create and recreate the virtual environment.

> The environment will be create in your home directory:

> `$PROJECT_NAME` and `$PYTHON_VERSION` are variables defined in the Makefile

```bash
$HOME/.pyenv/versions/$PROJECT_NAME-$PYTHON_VERSION/bin/python

/home/renan/.pyenv/versions/edu-loan-3.8.5/bin/python
```


### Run unit tests, style and convention

- Tests will run with coverage minimum at 80%.

Running code style
```bash
➜ make code-convention
```
Running unit tests
```bash
➜ make test
```
Running code style and all tests
```bash
➜ make
```

## How to run this project

There are some ways to run this project.

> When you create virtual environment, you have those 3 options above:

```bash
➜ flask run
```
or

```bash
➜ python wsgi.py
```
or 

```bash
➜ make run
```

The server is accessible at the link below, despite there is no root endpoint:
> http://127.0.0.1:5000/

The endpoints available are:
- **POST** http://127.0.0.1:5000/api/v1/event-flow

- **POST** http://127.0.0.1:5000/api/v1/auth/register
- **POST** http://127.0.0.1:5000/api/v1/auth/login


- **POST** http://127.0.0.1:5000/api/v1/users/cpf
- **POST** http://127.0.0.1:5000/api/v1/users/full-name
- **POST** http://127.0.0.1:5000/api/v1/users/birthday
- **POST** http://127.0.0.1:5000/api/v1/users/phone
- **POST** http://127.0.0.1:5000/api/v1/users/address
- **POST** http://127.0.0.1:5000/api/v1/users/amount

---
## Usage examples

### cURL
**Creates the event flow**

The idea here is that, each event represents the last part of the users endpoints. So this endpoint must be the first one executed, prior to any user registrations. 

```bash
➜ curl -X POST http://127.0.0.1:5000/api/v1/event-flow -d '{"event_flow": ["cpf", "full-name", "birthday", "phone", "address", "amount"]}' -H 'Content-Type: application/json'
```

**Registers a user**

```bash
➜ curl -X POST http://127.0.0.1:5000/api/v1/auth/register -d '{"email": "juca@juca.com", "password": "mypass"}' -H 'Content-Type: application/json'
```

**Login a user**

```bash
➜ curl -X POST http://127.0.0.1:5000/api/v1/auth/login -d '{"email": "juca@juca.com", "password": "mypass"}' -H 'Content-Type: application/json'
```

**Adds user CPF**

```bash
➜ curl -X POST http://127.0.0.1:5000/api/v1/users/cpf -d '{"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Imp1Y2FAanVjYS5jb20ifQ.RYgkYNzp43tXo9xLDfUFu4w4EMjuGhgjmZEv7WA16cY", "data": "68077335004"}' -H 'Content-Type: application/json'
```

**Adds user Full Name**

```bash
➜ curl -X POST http://127.0.0.1:5000/api/v1/users/full-name -d '{"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Imp1Y2FAanVjYS5jb20ifQ.RYgkYNzp43tXo9xLDfUFu4w4EMjuGhgjmZEv7WA16cY", "data": "Juca da Silva"}' -H 'Content-Type: application/json'
```

**Adds user Birthday**

```bash
➜ curl -X POST http://127.0.0.1:5000/api/v1/users/birthday -d '{"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Imp1Y2FAanVjYS5jb20ifQ.RYgkYNzp43tXo9xLDfUFu4w4EMjuGhgjmZEv7WA16cY", "data": "2020-03-07"}' -H 'Content-Type: application/json'
```

**Adds user Phone**

```bash
➜ curl -X POST http://127.0.0.1:5000/api/v1/users/phone -d '{"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Imp1Y2FAanVjYS5jb20ifQ.RYgkYNzp43tXo9xLDfUFu4w4EMjuGhgjmZEv7WA16cY", "data": "51999999999"}' -H 'Content-Type: application/json'
```

**Adds user Address**

```bash
➜ curl -X POST http://127.0.0.1:5000/api/v1/users/address -d '{"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Imp1Y2FAanVjYS5jb20ifQ.RYgkYNzp43tXo9xLDfUFu4w4EMjuGhgjmZEv7WA16cY", "data": "88035150,servid,22,apto 605,floripa,sc"}' -H 'Content-Type: application/json'
```

**Adds user Amount**

```bash
➜ curl -X POST http://127.0.0.1:5000/api/v1/users/amount -d '{"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Imp1Y2FAanVjYS5jb20ifQ.RYgkYNzp43tXo9xLDfUFu4w4EMjuGhgjmZEv7WA16cY", "data": "123"}' -H 'Content-Type: application/json'
```
