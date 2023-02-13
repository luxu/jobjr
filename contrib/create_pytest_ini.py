import os

filename = "pytest.ini"

# Pega o diretório raiz do projeto
path = os.path.normpath(os.path.abspath(__file__) + os.sep + os.pardir)
path_dir_raiz = "/".join(path.split("\\")[:-1])
path_dir = path.split("\\")[-2]
print(path_dir_raiz)

PYTEST = """
[pytest]
addopts = --ds=%s.settings --reuse-db -p no:warnings
python_files = tests.py test_*.py
""".strip() % (
    path_dir
)

path_file = os.path.join(path_dir_raiz, filename)
print(path_file)

with open(path_file, "w") as _f:
    r = _f.write(PYTEST)
