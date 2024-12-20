# main.py
from fastapi import FastAPI, Depends, HTTPException
from datetime import date
from sqlalchemy.orm import Session, joinedload
from typing import List
from local_stage import save_local_stage
from models.models import Unidade, Paciente, Leito, Transferencia, Alta, Atendimento, Profissional # Importa os models
from database import SessionLocal, engine, Base  # Importa a sessão e a engine do database.py
from pydantic import BaseModel
from sqlalchemy.exc import OperationalError, DatabaseError

#importando controllers
from controllers.altaController import router as alta_router
from controllers.atendimentoController import router as atendimento_router
from controllers.leitoController import router as leito_router
from controllers.pacienteController import router as paciente_router
from controllers.profissionalController import router as profissional_router
from controllers.testController import router as test_router
from controllers.transferenciaController import router as transferencia_router
from controllers.unidadeController import router as unidade_router

# Cria o aplicativo FastAPI
app = FastAPI()

#====== Rota Publica apenas para testar no Postman se esta tudo funcionando======
@app.get("/")
def root():
    return {"message": "API esta funcionando!"}

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Dependência que fornece uma sessão de banco de dados para cada requisição
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Adicionando as rotas
app.include_router(alta_router)
app.include_router(atendimento_router)
app.include_router(leito_router)
app.include_router(paciente_router)
app.include_router(profissional_router)
app.include_router(test_router)
app.include_router(transferencia_router)
app.include_router(unidade_router)
