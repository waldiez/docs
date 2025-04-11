.DEFAULT_GOAL := help

.TESTS_DIR := tests
.REPORTS_DIR := reports
.PACKAGE_NAME := waldiez

.PHONY: help
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Default target: help"
	@echo ""
	@echo "Targets:"
	@echo " help             Show this message and exit"
	@echo " format           Format the code"
	@echo " lint             Lint the code"
	@echo " forlint          Alias for 'make format && make lint'"
	@echo " clean            Clean unnecessary files"
	@echo " patch            Apply patches to the jupyter_contrib_nbextensions package"
	@echo " docs             Generate the documentation"
	@echo " docs-live        Generate the documentation in 'live' mode"
	@echo ""

.PHONY: format
format:
	python scripts/format.py

.PHONY: lint
lint:
	python scripts/lint.py

.PHONY: forlint
forlint: format lint

.PHONY: clean
clean:
	python scripts/clean.py

.PHONY: patch
patch:
	python scripts/patch.py

.PHONY: docs
docs: patch
	python -m mkdocs build -d site
	@echo "open:   file://`pwd`/site/index.html"
	@echo "or use: \`python -m http.server --directory site\`"

.PHONY: docs-live
docs-live: patch
	python -m mkdocs serve --watch mkdocs.yaml --watch src --dev-addr localhost:8400
