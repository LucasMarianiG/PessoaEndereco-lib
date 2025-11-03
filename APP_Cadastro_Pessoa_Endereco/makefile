# Variáveis
PACKAGE_NAME=pessoa-endereco-lib
VERSION=0.1.0

# Instalar dependências gerais (FastAPI, Uvicorn, etc.)
install:
	python -m pip install -r requirements.txt

# Instalar dependências de desenvolvimento (build, wheel, twine, pytest, etc.)
install-dev:
	python -m pip install -r requirements.txt
	python -m pip install wheel build twine pytest

# Instalar a lib calculator-lib do PyPI
install-lib:
	python -m pip install $(PACKAGE_NAME)

# Rodar testes da aplicação FastAPI
test-app:
	pytest tests/

# Rodar testes da biblioteca calculator-lib
test-lib:
	pytest tests_lib/

# Buildar a lib para publicação (modo tradicional)
build-lib:
	python setup.py sdist bdist_wheel

# Buildar a lib usando ferramenta moderna
build-modern:
	python -m build

# Publicar a lib no PyPI
publish-lib: build-modern
	python -m twine upload dist/*

# Limpar artefatos de build
clean:
	rm -rf build dist *.egg-info

# Buildar os containers usando docker compose
docker-build:
	docker compose build

# Subir a aplicação usando docker compose
docker-up:
	docker compose up

# Subir a aplicação em modo detached (background)
docker-up-detached:
	docker compose up -d

# Derrubar a aplicação
docker-down:
	docker compose down

# Limpar imagens, volumes, containers órfãos
docker-clean:
	docker compose down --rmi all --volumes --remove-orphans

# Mostrar ajuda
help:
	@echo "Comandos disponíveis:"
	@echo "  make install            - Instalar dependências gerais"
	@echo "  make install-lib        - Instalar a lib pessoa-endereco-lib do PyPI"
	@echo "  make install-dev        - Instalar ferramentas de build/teste"
	@echo "  make test-lib           - Rodar testes da biblioteca"
	@echo "  make test-app           - Rodar testes da API"
	@echo "  make build-lib          - Buildar lib tradicional (setup.py)"
	@echo "  make build-modern       - Buildar lib moderno (python -m build)"
	@echo "  make publish-lib        - Publicar lib"
	@echo "  make docker-build       - Buildar containers com docker compose"
	@echo "  make docker-up          - Subir aplicação com docker compose"
	@echo "  make docker-up-detached - Subir aplicação em background"
	@echo "  make docker-down        - Derrubar aplicação"
	@echo "  make docker-clean       - Limpar containers, imagens e volumes"