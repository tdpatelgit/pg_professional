# PG Professional (PGPro / PP)
Python-flask based web application to manage "Paying Guest" accomodation business. It features options like displaying rental plans, managing rents, accounting expenses etc.

## How it works?
It a hosted webapp that can be accessed from any latest web browers.

## Contribute to development
Its a public code and everyone is welcome to contribute to it. Once you are developing changes for the repo, you need to follow instruction in this section very carefully. Once you have completed changes, try running local CI checks to avoid failures on repository CI actions.

### Setup virtual environment
You need to install `pipenv` package on system which is used for development. Once pipenv is install you need to create virtual environment with below commands.

```bash
# Install virtual environment with all development package dependencies.
pipenv install --dev
```

To run code on production without devlopment packages.
```bash
# Install virtual environment without development package, it can only be used only for running production code but not performing any development checks.
pipenv install
```

### Run Code Style Check
Run the below command to perform code style check.

```bash
pipenv run pycodestyle src/
```

### Run Document Style Check
Run the below command to perform document style check.

```bash
pipenv run pydocstyle src/
```

### Run Linter Check
Run the below command to perform linter check.

```bash
pipenv run pylint src/
```

### Run Development server locally
Run the below command to run flask service locally on http://127.0.0.1:5000

```bash
pipenv run python -m src.server
```

