"""Smoke test for the published package.

This script demonstrates importing the package modules, creating the DB schema
and inserting a Pessoa + Endereco record using the bundled utilities.

Run after installing dependencies and the package (see example/README.md).
"""
from util.database import init_db, engine
from sqlmodel import Session
from model.models import Pessoa, Endereco


def main():
    print("Initializing database (creates ./app.db)...")
    init_db()

    with Session(engine) as session:
        p = Pessoa(nome="Smoke Tester", idade="30", email="smoke@example.com")
        session.add(p)
        session.commit()
        session.refresh(p)
        print("Inserted Pessoa id:", p.id, "nome:", p.nome)

        e = Endereco(logradouro="Rua do Teste", numero="100", cidade="CidadeX", bairro="Centro", estado="ES", pessoa_id=p.id)
        session.add(e)
        session.commit()
        session.refresh(e)
        print("Inserted Endereco id:", e.id, "cidade:", e.cidade)


if __name__ == "__main__":
    main()
