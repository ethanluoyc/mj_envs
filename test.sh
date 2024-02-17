
python3.10 -m venv test_env
source test_env/bin/activate

pip install pytest -r requirements.txt .
cd tests
pytest .
