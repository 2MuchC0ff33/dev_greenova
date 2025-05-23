.PHONY: app install install-dev install-prod compile sync sync-prod venv dotenv-pull dotenv-push check run run-django run-tailwind compile-proto check-tailwind tailwind tailwind-install update update-recurring-dates normalize-frequencies clean-csv prod lint-templates format-templates check-templates format-lint

# Change to greenova directory before running commands
CD_CMD = cd greenova &&

# Define the virtual environment path
VENV = .venv

# Define the python and pip path
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

# Variables
REQUIREMENTS=requirements/requirements.txt
DEV_REQUIREMENTS=requirements/requirements-dev.txt
PROD_REQUIREMENTS=requirements/requirements-prod.txt
CONSTRAINTS=requirements/constraints.txt
SETUP_SCRIPT=setup.py

# Create virtual environment
venv:
	@echo "Creating virtual environment..."
	@python3 -m venv $(VENV)
	@echo "Virtual environment created."
	@echo "To activate it, run: source .venv/bin/activate"

# Install dependencies
install:
	@echo "Installing dependencies..."
	$(PYTHON) -m pip install --upgrade pip
	$(PIP) install pip-tools
	$(PIP) install -r $(REQUIREMENTS) -c $(CONSTRAINTS)
	@echo "Dependencies installed."

install-dev:
	@echo "Installing dev dependencies..."
	$(PYTHON) -m pip install --upgrade pip
	$(PIP) install pip-tools
	$(PIP) install -r $(REQUIREMENTS) -r $(DEV_REQUIREMENTS) -c $(CONSTRAINTS)
	@echo "Dev dependencies installed."

install-prod:
	@echo "Installing prod dependencies..."
	$(PYTHON) -m pip install --upgrade pip
	$(PIP) install pip-tools
	$(PIP) install -r $(REQUIREMENTS) -r $(PROD_REQUIREMENTS) -c $(CONSTRAINTS)
	@echo "Prod dependencies installed."

# Compile requirements files
compile:
	@echo "Compiling requirements..."
	$(VENV)/bin/pip-compile requirements/requirements.in
	$(VENV)/bin/pip-compile requirements/requirements-dev.in
	$(VENV)/bin/pip-compile requirements/requirements-prod.in
	$(VENV)/bin/pip-compile --all-build-deps --all-extras --output-file=requirements/constraints.txt --strip-extras requirements/requirements.in
	@echo "Requirements compiled."

# Sync environment to requirements
sync:
	@echo "Syncing environment to requirements..."
	$(VENV)/bin/pip-sync requirements/requirements.txt requirements/requirements-dev.txt -c requirements/constraints.txt
	@echo "Environment synced."

sync-prod:
	@echo "Syncing environment to production requirements..."
	$(VENV)/bin/pip-sync requirements/requirements.txt requirements/requirements-prod.txt -c requirements/constraints.txt
	@echo "Production environment synced."

# Freeze installed dependencies to requirements.txt
freeze:
	@echo "Freezing dependencies..."
	$(VENV)/bin/pip freeze > $(REQUIREMENTS)
	@echo "Dependencies frozen."

# Create a Django new app
app:
	@if [ -z "$(name)" ]; then echo "Error: Please provide app name with 'make app name=yourappname'"; exit 1; fi
	$(CD_CMD) python3 manage.py startapp $(name)

# Pull .env file from dotenv-vault
dotenv-pull:
	@echo "Pulling .env file from dotenv-vault"
	@npx dotenv-vault@latest pull

# Push .env file to dotenv-vault
dotenv-push:
	@echo "Pushing .env file to dotenv-vault"
	@npx dotenv-vault@latest push

# Validate the presence of the .env file before running checks
check:
	@if [ ! -f .env ]; then \
		echo "Error: .env file is missing. Please create it and set the required environment variables."; \
		exit 1; \
	fi
	$(CD_CMD) python3 manage.py check

# Updated run command with better process management and gunicorn config
run:
	@echo "Starting Django server with pre-built Tailwind CSS..."
	@mkdir -p logs
	@cd /workspaces/greenova/greenova/theme/static_src && node build-tailwind.js > ../../logs/tailwind_build.log 2>&1 || (cat ../../logs/tailwind_build.log && exit 1)
	@echo "Tailwind CSS built successfully"
	@$(CD_CMD) python3 manage.py runserver 0.0.0.0:8000

# Alternative approach with separate commands
# Start only Django server
run-django:
	$(CD_CMD) gunicorn greenova.wsgi -c ../gunicorn.conf.py

# Start only Tailwind CSS
run-tailwind:
	$(CD_CMD) python3 manage.py tailwind start

# Check Tailwind installation status
check-tailwind:
	$(CD_CMD) python3 manage.py tailwind check-updates

# Tailwind commands
# Build Tailwind CSS
tailwind-build:
	$(CD_CMD) python3 manage.py tailwind build

# Add a Tailwind install command
tailwind-install:
	$(CD_CMD) python3 manage.py tailwind install

# Update data from CSV file
update:
	$(CD_CMD) python3 manage.py import_obligations dummy_data.csv --force-update

# Update recurring inspection dates
update-recurring-dates:
	$(CD_CMD) python3 manage.py update_recurring_inspection_dates

# Normalize existing frequencies
normalize-frequencies:
	$(CD_CMD) python3 manage.py normalize_existing_frequencies

# Clean CSV file
clean-csv:
	$(CD_CMD) python3 manage.py clean_csv_to_import dirty.csv

# Compile proto file
compile-proto:
	$(CD_CMD) python3 manage.py compile_proto

# Run production server
prod:
	$(CD_CMD) /bin/sh scripts/prod_urls.sh

# Used to pre-compile Tailwind CSS before running the application (we should maybe use this in run later)
tailwind:
	$(CD_CMD) python3 manage.py tailwind start

# Template linting commands
# Lint Django template files
lint-templates:
	djlint greenova/**/templates --lint

# Format Django template files
format-templates:
	djlint greenova/**/templates --reformat

# Check template formatting without changes
check-templates:
	djlint greenova/**/templates --check

# Combined command for formatting and linting
format-lint: format-templates lint-templates

# Remove virtual environment and temporary files
clean:
	@echo "Removing virtual environment and temporary files..."
	@rm -rf $(VENV)
	@find . -name "*.pyc" -delete
	@find . -name "__pycache__" -delete
	@echo "Clean completed."

# Install the package with setup.py
setup:
	@echo "Running setup.py..."
	$(PYTHON) $(SETUP_SCRIPT) install

# Run Python startup script
pythonstartup:
	@echo "Setting up Python startup..."
	$(PYTHON) -M pythonstartup

# Install setuptools
setuptools:
	@echo "Installing setuptools..."
	$(PYTHON) -m pip install setuptools

# Help command to list available commands
help:
	@echo "Available commands:"
	@echo "  make app name=appname - Create a new Django app with the specified name"
	@echo "  make check        - Run Django system check framework"
	@echo "  make check-templates  - Check template formatting without changes"
	@echo "  make format-templates - Format Django template files"
	@echo "  make prod         - Run production server"
	@echo "  make lint-templates   - Lint Django template files"
	@echo "  make update       - Update data from CSV file"
	@echo "  make update-recurring-dates - Update recurring inspection dates"
	@echo "  make normalize-frequencies - Normalize existing frequencies"
	@echo "  make clean-csv     - Clean CSV file"
	@echo "  make tailwind     - Start Tailwind CSS server"
	@echo "  make venv           - Create virtual environment"
	@echo "  make install        - Install dependencies"
	@echo "  make install-dev    - Install dev dependencies"
	@echo "  make install-prod   - Install prod dependencies"
	@echo "  make compile        - Compile requirements files"
	@echo "  make sync           - Sync environment to requirements"
	@echo "  make sync-prod      - Sync environment to production requirements"
	@echo "  make clean          - Remove virtual environment and clean temporary files"
	@echo "  make freeze		 - Freeze dependencies"
	@echo "  make dotenv-pull	 - Pull .env file from dotenv-vault"
	@echo "  make dotenv-push	 - Push .env file to dotenv-vault"
	@echo "  make setup			 - Install the package with setup.py"
	@echo "  make pythonstartup	 - Run Python startup script"
	@echo "  make setuptools	 - Install setuptools"
