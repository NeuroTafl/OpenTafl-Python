# Incredibly simple makefile for install & cleanup
# Aaron S. Crandall <crandall@gonzaga.edu>
# Copyright: 2022

ENGINES_DIR=../OpenTafl/engines
NEUROTAFL_DIR=$(ENGINES_DIR)/NeuroTafl

OPENTAFL_LIB_FILE=OpenTaflAgent.py

DUMMY_AGENT=OneMoveAgent.py
DUMMY_INI=OneMoveAgent.ini

TENSOR_AGENT=TensorAgent-V1.py
TENSOR_INI=TensorAgentV1.ini


all:
	@echo "Nothing really done for all"
	@echo " See other Makefile targets (install)"

install: install-onemove-agent
install: install-tensor-agent

create-NeuroTafl-dir:
	@echo "Creating NeuroTafl scripts directory in OpenTafl server engines"
	mkdir -p $(NEUROTAFL_DIR)

install-lib: create-NeuroTafl-dir
	@echo "Copying main OpenTaflAgent module (lib) into place"
	cp $(OPENTAFL_LIB_FILE) $(NEUROTAFL_DIR)
	cp MoveDecider.py $(NEUROTAFL_DIR)
	cp Board.py $(NEUROTAFL_DIR)
	cp Coordinate.py $(NEUROTAFL_DIR)
	cp Move.py $(NEUROTAFL_DIR)
	cp Ply.py $(NEUROTAFL_DIR)
	cp TensorMoveDecider.py $(NEUROTAFL_DIR)

install-onemove-agent: install-lib create-NeuroTafl-dir
	@echo "Installing One Move dummy / test agent"
	cp $(DUMMY_INI) $(ENGINES_DIR)
	cp $(DUMMY_AGENT) $(NEUROTAFL_DIR)

install-tensor-agent: install-lib create-NeuroTafl-dir
	@echo "Installing One Move dummy / test agent"
	cp $(TENSOR_INI) $(ENGINES_DIR)
	cp $(TENSOR_AGENT) $(NEUROTAFL_DIR)

uninstall:

	rm $(ENGINES_DIR)/$(DUMMY_INI)
	rm $(ENGINES_DIR)/$(TENSOR_INI)
	rm -r $(NEUROTAFL_DIR)

test:
	@echo "Running pytest on whole suite"
	pytest

black:
	@echo "Should run black to lint/format all files"
	black .

lint:
	@echo "Running lint with flake8"
	flake8 . --count --exit-zero --max-line-length=100 --statistics

clean:
	rm -r __pycache__
	rm -r .pytest_cache

install-deps:
	pip3 install -r requirements.txt
