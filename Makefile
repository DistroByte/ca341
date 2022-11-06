# Top level makefile, enter directories and make

PYTHON = python3
.DEFAULT_GOAL = help

help:
	@echo "-------------------HELP-------------------"
	@echo "To run the python code, type 'make python'"
	@echo "To run the C code, type 'make C'"
	@echo "------------------------------------------"

python:
	@echo "----------PYTHON----------"
	@echo "Running python code..."
	@echo "--------------------------"
	$(PYTHON) python/oop.py

C:
	@echo "----------C----------"
	@echo "Running C code..."
	@echo "---------------------"
	$(MAKE) -C C

clean:
	@echo "----------CLEAN----------"
	@echo "Cleaning up..."
	@echo "-------------------------"
	$(MAKE) -C C clean

.PHONY: python C clean help