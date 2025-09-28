# =================================================================
#  1. CORREÇÃO DE PATH PARA A VERCEL
#  Este trecho é essencial para que a Vercel encontre seus módulos
#  em outras pastas, como a pasta "Matching".
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
#  A linha abaixo foi comentada porque as bibliotecas que ela usa
#  (spacy, scikit-learn) são muito grandes para o plano gratuito
#  da Vercel e causam falha no build.
# =================================================================
# from Matching.pipeline import MatchingPipeline


# Inicializa a aplicação FastAPI
app = FastAPI()

@app.post("/match_vaga")
async def match_vaga(descricao: str = Form(...)):
    """
    Recebe a descrição de uma única vaga e deveria retornar os matches.
    A lógica de matching real foi desabilitada para permitir o deploy.
    """
    try:
        # A lógica de matching original está comentada.
        # pipeline = MatchingPipeline()
        # matches = pipeline.matching_process(descricao)

        # Resposta temporária (placeholder):
        matches = {
            "status": "sucesso",
            "mensagem": "A API está no ar, mas a funcionalidade de matching está temporariamente desabilitada devido a restrições do deploy.",
            "descricao_recebida": descricao[:100] + "..." # Mostra um trecho do que foi recebido
        }
        return JSONResponse(content=matches)

    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": f"Ocorreu um erro inesperado: {str(e)}"})


@app.post("/match_vagas")
async def match_vagas(file: UploadFile = File(...)):
    """
    Recebe um arquivo JSON com múltiplas vagas e deveria retornar os matches.
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
            "mensagem": "A API recebeu o arquivo, mas a funcionalidade de matching está temporariamente desabilitada.",
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
    return {"mensagem": "Bem-vindo à API da Decision HR. O frontend deve ser servido neste mesmo endereço."}