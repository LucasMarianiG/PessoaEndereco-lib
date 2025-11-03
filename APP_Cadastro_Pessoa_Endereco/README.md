# cadastroPessoaEndereco-Lib

Biblioteca para gerenciar cadastro de Pessoas e Endereços usando FastAPI + SQLModel.

Este repositório contém o código-fonte, testes unitários e instruções para publicar/utilizar a biblioteca.

Principais componentes
- Modelos: `APP_PessoaEndereco/model/models.py` (classes Pessoa e Endereco usando SQLModel)
- Banco: `APP_PessoaEndereco/util/database.py` (inicialização do SQLite e engine)
- Testes: `APP_PessoaEndereco/test` (pytest)

Recursos
- CRUD básico (modelos e camada de repositório)
- Exemplo rápido para inicializar o banco e inserir registros (smoke test)

Instalação

1) Usando o PyPI (recomendado para quem só quer usar a biblioteca):

```powershell
# criar e ativar um venv (PowerShell)
python -m venv .venv
. .\.venv\Scripts\Activate.ps1

# instalar a biblioteca publicada e dependências úteis
python -m pip install --upgrade pip
python -m pip install cadastroPessoaEndereco-lib sqlmodel fastapi
```

2) A partir do código-fonte (para desenvolvimento):

```powershell
# entrar na raiz do projeto (onde está setup.py)
cd APP_Cadastro_Pessoa_Endereco
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# instalar em modo editable (opcional)
python -m pip install -e .
```

Uso rápido (smoke test)

O exemplo abaixo cria o banco SQLite (`app.db`), insere uma `Pessoa` e um `Endereco` e imprime os IDs criados.

Crie o arquivo `smoke_test.py` com este conteúdo (ou copie o trecho):

```python
from APP_PessoaEndereco.util.database import init_db, engine
from sqlmodel import Session
from APP_PessoaEndereco.model.models import Pessoa, Endereco

def main():
	init_db()
	with Session(engine) as session:
		p = Pessoa(nome="Smoke Tester", idade="30", email="smoke@example.com")
		session.add(p)
		session.commit()
		session.refresh(p)
		print("Pessoa id:", p.id, "nome:", p.nome)
		e = Endereco(logradouro="Rua do Teste", numero="100", cidade="CidadeX", bairro="Centro", estado="ES", pessoa_id=p.id)
		session.add(e)
		session.commit()
		session.refresh(e)
		print("Endereco id:", e.id, "cidade:", e.cidade)

if __name__ == "__main__":
	main()
```

Execute no PowerShell (com o venv ativado):

```powershell
python smoke_test.py
```

Rodando os testes

Os testes usam `pytest`. Para executar:

```powershell
# ativar venv (se ainda não estiver)
. .\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pip install pytest
python -m pytest -q
```

Publicação

Se quiser publicar no PyPI:

1. Atualize a versão em `setup.py`.
2. Gere os artefatos:

```powershell
python -m build
```

3. Faça o upload com `twine` (use token, preferencialmente via variável de ambiente TWINE_PASSWORD ou TWINE_USERNAME/TWINE_PASSWORD):

```powershell
python -m twine upload dist/*
```

Boas práticas e notas
- O pacote depende de `sqlmodel` (SQLAlchemy + Pydantic). Ao publicar, considere declarar `install_requires` em `setup.py` para que `pip` instale automaticamente as dependências.
- Arquivos principais do projeto estão em `APP_PessoaEndereco/`.

Contribuindo

1. Faça um fork e branch para sua feature/bugfix.
2. Abra um pull request com descrição clara e testes quando aplicável.

Licença

Este projeto inclui um arquivo `LICENSE` (MIT). Consulte-o para detalhes.

Contato

Para dúvidas, abra uma issue neste repositório.
