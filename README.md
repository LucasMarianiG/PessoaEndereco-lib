# API Pessoa & Endereço

Projeto de exemplo em FastAPI + SQLModel para gerenciar Pessoas e Endereços usando um padrão MVC leve (Controllers → Services → Repositories). O código disponibiliza rotas CRUD para `pessoas` e `enderecos` e foi desenhado para ser simples de aprender e estender.

## Estrutura principal

- `APP_PessoaEdereco/main.py` — ponto de entrada da aplicação
- `APP_PessoaEdereco/util/database.py` — criação do engine e sessão (SQLite por padrão)
- `APP_PessoaEdereco/model/models.py` — modelos SQLModel (Pessoa, Endereco)
- `APP_PessoaEdereco/model/dto.py` — schemas/DTOs (create/read/update/public)
- `APP_PessoaEdereco/controller/Pessoa.py` — rotas/Controller para pessoas (`/pessoas`)
- `APP_PessoaEdereco/controller/Endereco.py` — rotas/Controller para endereços (`/enderecos`)

O projeto traz um `requirements.txt` com as versões usadas. Principais pacotes:

- fastapi
- uvicorn
- sqlmodel (SQLAlchemy + Pydantic)

## Como clonar o repositório

No PowerShell (Windows):

```powershell
git clone https://github.com/LucasMarianiG/APP_Cadastro_Pessoa_Endereco.git 
cd meu-projeto-pessoa-endereco


---

## 🔌 Endpoints (principais)

Pessoas — Base path: `/pessoas`

| Método | Rota            | Body           | Resposta         | Descrição                          |
| ------ | --------------- | -------------- | ---------------- | ---------------------------------- |
| POST   | `/pessoas/`     | `PessoaCreate` | `PessoaRead`     | Cria uma pessoa                    |
| GET    | `/pessoas/`     | —              | `List[PessoaRead]` | Lista pessoas (offset/limit)     |
| GET    | `/pessoas/{id}` | —              | `PessoaRead`     | Busca pessoa por ID                |
| PATCH  | `/pessoas/{id}` | `PessoaUpdate` | `PessoaRead`     | Atualiza campos parciais           |
| DELETE | `/pessoas/{id}` | —              | `204 No Content` | Remove pessoa                      |

Endereços — Base path: `/enderecos`

| Método | Rota              | Body            | Resposta         | Descrição                          |
| ------ | ----------------- | --------------- | ---------------- | ---------------------------------- |
| POST   | `/enderecos/`     | `EnderecoCreate`| `EnderecoRead`   | Cria um endereço (assoc. a pessoa) |
| GET    | `/enderecos/`     | —               | `List[EnderecoRead]` | Lista endereços                |
| GET    | `/enderecos/{id}` | —               | `EnderecoRead`   | Busca endereço por ID              |
| PATCH  | `/enderecos/{id}` | `EnderecoUpdate`| `EnderecoRead`   | Atualiza campos parciais           |
| DELETE | `/enderecos/{id}` | —               | `204 No Content` | Remove endereço                    |

---


## 🧠 Como as camadas se conectam

```
HTTP (FastAPI)
   ↓
Controller (APP_PessoaEdereco/controller)
   ↓
Service (APP_PessoaEdereco/service)
   ↓
Repository (APP_PessoaEdereco/repository)
   ↓
DB Session (APP_PessoaEdereco/util/database.py) + SQLModel (APP_PessoaEdereco/model/models.py)
```

* **Controller**: lida com requisições/respostas e validações de query/path; injeta dependências com `Depends`.
* **Service**: regras de negócio (ex.: validações e regras antes de persistir).
* **Repository**: acesso ao banco via SQLModel/SQLAlchemy (CRUD genérico).
* **Database**: engine, sessão e criação de schema.

## Reference:
[Documento Fast API](https://fastapi.tiangolo.com/) : Documentação do FAST API. 
```

## Contribuições

Abra issues e pull requests. Para novidades, descreva o problema e passos para reproduzir.

---

Se quiser, adapto este README para incluir comandos Git, CI simples ou instruções para deploy em Docker/Heroku/Azure/GCP. Basta pedir.

---

## ✨ Principais recursos

* Estrutura limpa em camadas (**Controller → Service → Repository → DB**)
* **SQLModel** (tipagem forte + ORM)
* Injeção de dependência com `Depends`
* Tratamento de erros HTTP padronizado
* Pronto para trocar **SQLite** por **PostgreSQL**

---

## 📂 Estrutura do projeto

```
APP_PessoaEdereco/
├─ controller/
│  ├─ Endereco.py
│  ├─ generic.py
│  └─ Pessoa.py
├─ model/
│  ├─ dto.py
│  └─ models.py
├─ repository/
│  └─ base.py
├─ service/
│  └─ base.py
├─ util/
│  └─ database.py
└─ main.py
```

---

## 🧰 Stack & Requisitos

* Python 3.10+
* FastAPI
* SQLModel

```
fastapi==0.114.2
uvicorn[standard]==0.30.6
SQLModel==0.0.22
```

> Para PostgreSQL, adicione também: `psycopg[binary]==3.*`

---

## ⚙️ ------------Configuração & Execução----------

1. Crie o ambiente e instale dependências:

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install "fastapi[standard]"
python.exe -m pip install --upgrade pip #Caso precise de uma atualização
pip install sqlmodel
fastapi dev .\APP_PessoaEdereco\main.py
```

2. (Opcional) Defina o banco via variável de ambiente:

* **SQLite (padrão)** – já funciona sem configurar nada.
* **PostgreSQL**:

  ```bash
  export DATABASE_URL="postgresql+psycopg://app:app@localhost:5432/appdb"
  ```

3. Rode a aplicação:

```bash
uvicorn app.main:app --reload
```

4. Acesse:

* Healthcheck: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* Docs (Swagger): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Reference:
[Documento Fast API](https://fastapi.tiangolo.com/) : Documentação do FAST API. 
