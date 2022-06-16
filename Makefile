# Incredibly simple makefile for install & cleanup
# Aaron S. Crandall <crandall@gonzaga.edu>
# Copyright: 2022

ENGINES_DIR=../OpenTafl/engines
SCRIPT_NAME=OpenTafl-python.py
INI_FILE=OpenTafl-python.ini
NEUROTAFL_DIR=$(ENGINES_DIR)/NeuroTafl

all:
	@echo "Nothing really done for all"
	@echo " See other Makefile targets"

install:
	cp $(INI_FILE) $(ENGINES_DIR)
	mkdir -p $(NEUROTAFL_DIR)
	cp $(SCRIPT_NAME) $(NEUROTAFL_DIR)

uninstall:
	rm $(ENGINES_DIR)/$(INI_FILE)
	rm -r $(NEUROTAFL_DIR)

test:
	@echo "Should run pytest"

black:
	@echo "Should run black"
	black $(SCRIPT_NAME)
