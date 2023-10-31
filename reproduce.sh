# In case it's still there
rm -f poetry.lock
rm -rf .venv

# Install deps
poetry install

# Run script (poetry install)
echo "Running script with poetry install"
poetry run python script.py

# Remove local depencency
poetry remove mymodule

# Install with pip as editable
cd mymodule
pip install -e .

# Run script (pip install)
cd ..
echo "Running script with pip install"
poetry run python script.py
