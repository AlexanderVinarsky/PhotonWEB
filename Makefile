.PHONY: run install
.DEFAULT_GOAL := help

run:
	poetry run uvicorn main:app --host 127.0.0.1 --port 8001 --reload

install:
	@echo "Installing dependency $(LIBRARY)"
	poetry add $(LIBRARY)

uninstall:
	@echo "Uninstalling dependency $(LIBRARY)"
	poetry remove $(LIBRARY)

help:
	@echo "  make run"
	@echo "  make install LIBRARY=package"
	@echo "  make uninstall LIBRARY=package"
