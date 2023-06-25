dist: codedict/slices $(shell find codedict -type f -name "*.py") setup.py
	./setup.py sdist bdist_wheel

$(shell find codedict -type f -name "*.py"):
	@touch $@

setup.py:
	@touch setup.py

codedict/slices: codedict/tmp.zip
	rm -r codedict/slices/*
	split -b 32M codedict/tmp.zip codedict/slices/slice.

codedict/tmp.zip: $(shell find codedict/books -type f -name "*")
	cd codedict/books; zip -r ../tmp.zip *

$(shell find codedict/books -type f -name "*"):
	@touch $@

upload: dist
	twine upload dist/**

install: dist
	pip install ./dist/*.whl --force-reinstall