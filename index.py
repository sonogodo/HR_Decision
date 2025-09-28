# =================================================================
#  1. CORREÇÃO DE PATH PARA A VERCEL (MUITO IMPORTANTE)
#  Este trecho garante que o Python consiga encontrar módulos em 
#  outras pastas do seu projeto, como a pasta "Matching".
# =================================================================
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


# =================================================================
#  2. IMPORTS ORIGINAIS DO PROJETO
# =================================================================
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import json

# =================================================================
#  3. LÓGICA DE MATCHING DESABILITADA
#  A linha abaixo foi comentada pois as bibliotecas que ela usa 
#  (spacy, scikit-learn) são muito grandes para o plano gratuito 
#  da Vercel e impedem o deploy de funcionar.
# =================================================================
# from Matching.pipeline import MatchingPipeline


# Inicializa a aplicação FastAPI
app = FastAPI()

@app.post("/match_vaga")
async def match_vaga(descricao: str = Form(...)):
    """
    Recebe a descrição de uma única vaga.
    A lógica de matching real foi desabilitada para permitir o deploy.
    """
    try:
        # A lógica de matching original está comentada.
        # pipeline = MatchingPipeline()
        # matches = pipeline.matching_process(descricao)

        # Resposta temporária (placeholder) para indicar que a API está funcionando:
        matches = {
            "status": "sucesso",
            "mensagem": "API está no ar, mas a funcionalidade de matching está temporariamente desabilitada.",
            "descricao_recebida": descricao[:100] + "..."
        }
        return JSONResponse(content=matches)

    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": f"Ocorreu um erro inesperado: {str(e)}"})


@app.post("/match_vagas")
async def match_vagas(file: UploadFile = File(...)):
    """
    Recebe um arquivo JSON com múltiplas vagas.
    A lógica de matching real foi desabilitada para permitir o deploy.
    """
    try:
        # Lê o conteúdo do arquivo JSON enviado
        json_content = await file.read()
        vagas_data = json.loads(json_content)

        # A lógica de matching original está comentada.
        # pipeline = MatchingPipeline()
        # all_matches = {}
        # for vaga_id, vaga_info in vagas_data.items():
        #     descricao = vaga_info.get("descricao", "")
        #     if descricao:
        #         matches = pipeline.matching_process(descricao)
        #         all_matches[vaga_id] = matches

        # Resposta temporária (placeholder):
        all_matches = {
            "status": "sucesso",
            "mensagem": "API recebeu o arquivo, mas a funcionalidade de matching está temporariamente desabilitada.",
            "nome_do_arquivo": file.filename,
            "jobs_encontrados": len(vagas_data)
        }
        return JSONResponse(content=all_matches)

    except json.JSONDecodeError:
        return JSONResponse(status_code=400, content={"erro": "Arquivo JSON inválido."})
    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": f"Ocorreu um erro inesperado: {str(e)}"})


# Endpoint raiz opcional para confirmar que a API está funcionando
@app.get("/")
async def root():
    return {"mensagem": "Bem-vindo à API da Decision HR."}

# Handler para Vercel - usando Mangum para compatibilidade ASGI
try:
    from mangum import Mangum
    handler = Mangum(app)
except ImportError:
    # Fallback se mangum não estiver disponível
    def handler(request):
        return app