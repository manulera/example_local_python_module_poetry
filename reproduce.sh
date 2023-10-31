# Coloured text
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# In case it's still there
rm -f poetry.lock
rm -rf .venv

# Install deps
poetry install

# Run script (poetry install)
echo "${GREEN}Running script with poetry install${NC}"
poetry run python script.py

# Remove local depencency
poetry remove mymodule

# Install with pip as editable
cd mymodule
poetry run pip install -e .

# Run script (pip install)
cd ..
echo "${GREEN}Running script with pip install${NC}"
poetry run python script.py
