# FLASK SERVER IMPORTS
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import json
import platform

# HAYSTACK IMPORTS
import os
from haystack.document_stores import InMemoryDocumentStore
from haystack.utils import convert_files_to_docs
from haystack.nodes import Seq2SeqGenerator, RAGenerator, DensePassageRetriever, PreProcessor, TfidfRetriever, FARMReader
from haystack.pipelines import GenerativeQAPipeline, ExtractiveQAPipeline

# FLASK SERVER SET UP
app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)


lfqa_document_store = InMemoryDocumentStore(embedding_dim=128, return_embedding=True)
rag_document_store = InMemoryDocumentStore(embedding_dim=128, return_embedding=True)
extractive_document_store = InMemoryDocumentStore(embedding_dim=128, return_embedding=True)

lfqa_document_store.delete_documents()
rag_document_store.delete_documents()
extractive_document_store.delete_documents()

docs = convert_files_to_docs(dir_path='app/docs')

preprocessor = PreProcessor(
    clean_empty_lines=True,
    clean_whitespace=True,
    clean_header_footer=True,
    add_page_number=True
)

docs = preprocessor.process(docs)

lfqa_document_store.write_documents(docs)
rag_document_store.write_documents(docs)
extractive_document_store.write_documents(docs)

lfqa_retriever = DensePassageRetriever(
    document_store=lfqa_document_store,
    query_embedding_model="vblagoje/dpr-question_encoder-single-lfqa-wiki",
    passage_embedding_model="vblagoje/dpr-ctx_encoder-single-lfqa-wiki",
)
rag_retriever = DensePassageRetriever(
    document_store=rag_document_store,
    query_embedding_model="facebook/dpr-question_encoder-single-nq-base",
    passage_embedding_model="facebook/dpr-ctx_encoder-single-nq-base",
    use_gpu=True,
    embed_title=True,
)
extractive_retriever = TfidfRetriever(document_store=extractive_document_store)

lfqa_document_store.update_embeddings(retriever=lfqa_retriever)
rag_document_store.update_embeddings(retriever=lfqa_retriever)

lfqa_generator = Seq2SeqGenerator(model_name_or_path="vblagoje/bart_lfqa")
rag_generator = RAGenerator(
    model_name_or_path="facebook/rag-token-nq",
    use_gpu=True,
    top_k=1,
    max_length=200,
    min_length=2,
    embed_title=True,
    num_beams=2,
)
extractive_reader = FARMReader(
    model_name_or_path="deepset/roberta-base-squad2")

lfqa_pipe = GenerativeQAPipeline(
    generator=lfqa_generator, retriever=lfqa_retriever)
rag_pipe = GenerativeQAPipeline(
    generator=rag_generator, retriever=rag_retriever)
extractive_pipe = ExtractiveQAPipeline(
    reader=extractive_reader, retriever=extractive_retriever)

if platform.system() == 'Windows':
    os.system('webapp/index.html')
else:
    os.system('open webapp/index.html')


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Methods', '*')
    return response


@app.route('/')
def index():
    return "Hello :)"


class LFQAQuery(Resource):
    def post(self):
        try:
            data = request.data
            data = json.loads(data)
            query = data['query']
            maxAns = data['max-ans']
            maxDoc = data['max-doc']
            response = lfqa_pipe.run(
                query=query,
                params={"Generator": {"top_k": int(maxAns)}, "Retriever": {
                    "top_k": int(maxDoc)}}
            )
            answers = []
            for ans in response['answers']:
                answers.append(
                    {'answer': ans.answer, 'context': ans.context, 'score': ans.score, 'type': ans.type, 'meta': ans.meta})

            documents = []
            for doc in response['documents']:
                documents.append(
                    {'content': doc.content, 'score': doc.score, 'meta': doc.meta})

            return {"error": False, "answers": answers, "documents": documents}

        except Exception as e:
            return {"error": True, "msg": str(e)}


class RAGQuery(Resource):
    def post(self):
        try:
            data = request.data
            data = json.loads(data)
            query = data['query']
            maxAns = data['max-ans']
            maxDoc = data['max-doc']
            response = rag_pipe.run(
                query=query,
                params={"Generator": {"top_k": int(maxAns)}, "Retriever": {
                    "top_k": int(maxDoc)}}
            )
            answers = []
            for ans in response['answers']:
                answers.append(
                    {'answer': ans.answer, 'context': ans.context, 'score': ans.score, 'type': ans.type, 'meta': ans.meta})

            documents = []
            for doc in response['documents']:
                documents.append(
                    {'content': doc.content, 'score': doc.score, 'meta': doc.meta})

            return {"error": False, "answers": answers, "documents": documents}

        except Exception as e:
            return {"error": True, "msg": str(e)}


class ExtractiveQuery(Resource):
    def post(self):
        try:
            data = request.data
            data = json.loads(data)
            query = data['query']
            maxAns = data['max-ans']
            maxDoc = data['max-doc']
            response = extractive_pipe.run(
                query=query,
                params={"Reader": {"top_k": int(maxAns)}, "Retriever": {
                    "top_k": int(maxDoc)}}
            )
            answers = []
            for ans in response['answers']:
                answers.append(
                    {'answer': ans.answer, 'context': ans.context, 'score': ans.score, 'type': ans.type, 'meta': ans.meta})

            documents = []
            for doc in response['documents']:
                documents.append(
                    {'content': doc.content, 'score': doc.score, 'meta': doc.meta})

            return {"error": False, "answers": answers, "documents": documents}

        except Exception as e:
            return {"error": True, "msg": str(e)}


api.add_resource(LFQAQuery, '/lfqa-query')
api.add_resource(RAGQuery, '/rag-query')
api.add_resource(ExtractiveQuery, '/extractive-query')
