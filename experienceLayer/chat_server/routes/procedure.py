from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd
import faiss
from fastapi import APIRouter
from transformers import pipeline
import torch
from ..models.procedure_model import TextInputModel, ChatResponseModel

router = APIRouter()

@router.post('/procedimento/')
async def closest_procedure(body:TextInputModel) -> ChatResponseModel:

    query = body.message

    # reading data 
    texts = pd.read_csv('./data/02_processed/full_data.csv')['procedimento_principal'].unique()

    # model definitions
    model_name = 'all-MiniLM-L6-v2'
    llm_model_dir = './data/bertimbau/'
    embedding_model = SentenceTransformer(
        model_name, 
        cache_folder=llm_model_dir, 
        device='cpu'
    )

    # embedding texts
    embeddings = embedding_model.encode(texts)
    # converting embeddings to numpy array
    embeddings = np.array(embeddings).astype("float32")
    #creating faiss index
    d = embeddings.shape[1]  # embedding dimension
    index = faiss.IndexFlatL2(d)  # using l2 distance as metric
    index.add(embeddings) # adding embeddings to index


    # converting query to embedding
    query_embedding = embedding_model.encode([query]).astype("float32")

    # choosing the number of results
    k = 20
    
    # searching for the closest embeddings
    distances, indices = index.search(query_embedding, k)

    # returning the closest text and calibrating the threshold

    max_distance = 0.7 # max distance for a good match
    # if we cannot find a good match, ask the user to go to and emergency
    if distances[0][0] > max_distance:
        return ChatResponseModel(assistant="DIAGNOSTICO E/OU ATENDIMENTO DE URGENCIA EM CLINICA MEDICA")
    
    else:
        return ChatResponseModel(assistant=texts[indices[0][0]])

