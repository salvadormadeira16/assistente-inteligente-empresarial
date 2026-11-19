from fastapi import FastAPI

# Criar a aplicação
app = FastAPI(
    title="Assistente Inteligente Empresarial",
    description="Assistente virtual para apoio ao cliente.",
    version="1.0.0"
)

# Rota principal
@app.get("/")
def inicio():
    return {
        "mensagem": "O assistente empresarial está a funcionar!"    
        }