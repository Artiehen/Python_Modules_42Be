PYTHON = python3
VENV = venv
VENV_PYTHON = $(VENV)/bin/python
VENV_PIP = $(VENV)/bin/pip
CONFIG = config.txt
BUILD = build
MAZEGEN = mazegen
FLAKE8 = flake8
MAZEGEN_B_DIR = dist/mazegen-1.0.0-py3-none-any.whl
INSTALL_MAZEGEN = mazegen-1.0.0-py3-none-any.whl
MYPY = mypy
PDB = pdb
AMAZE = a_maze_ing.py
CACHE = __pycache__
MYPYCACHE = .mypy_cache
SOURCE = source

all: install lint run

install:
	pip install $(MYPY)
	pip install $(FLAKE8)
	pip install $(INSTALL_MAZEGEN)

# Creazione virtualenv
vrt:
	$(PYTHON) -m venv venv
	. venv/bin/activate
	$(VENV_PIP) install --upgrade pip
	$(VENV_PIP) install $(FLAKE8)
	$(VENV_PIP) install $(MYPY)
	$(VENV_PIP) install $(BUILD)

# 	venv/bin/python -m pip list -> check pip installation in virtual pip

# Esecuzione
run:
	$(PYTHON) $(AMAZE) $(CONFIG)

debug:
	$(PYTHON) -m $(PDB) $(AMAZE) $(CONFIG)

# Type checking
# typecheck: $(VENV)
# 	$(VENV)/bin/mypy a_maze_ing.py

build:
	
	$(PYTHON) -m $(BUILD)
	pip install $(MAZEGEN_B_DIR)

lint:
	$(PYTHON) -m $(FLAKE8)
	$(PYTHON) -m $(MYPY) . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

#added to build mazegenpackage


# Pulizia
clean:
	rm -rf $(VENV) $(CACHE) $(MYPYCACHE) maze.txt
	rm -rf ./mazegen/$(CACHE) ./mazegen.egg-info
	rm -rf ./dist ./mazegen.egg-info
	pip uninstall $(MAZEGEN) -y



re: clean all

.PHONY: all run lint clean re