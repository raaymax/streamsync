#!/bin/bash

# The script fails if any step fails
set -e

# UI BUILD

cd ./ui
npm run build
cd ..

# PYTEST

cd ./tests
poetry run pytest
cd ..

# TYPE CHECKS (MYPY)

poetry run  mypy ./src/streamsync/*.py

# APP PROVISIONING

rm -rf ./src/streamsync/app_templates/*
cp -r ./apps/default ./cli/src/streamsync/app_templates
cp -r ./apps/hello ./cli/src/streamsync/app_templates
cp -r ./apps/quickstart ./cli/src/streamsync/app_templates

# PYTHON PACKAGE BUILD

rm -rf ./dist/*
poetry build
