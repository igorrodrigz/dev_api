from flask import Flask, request
from flask_restful import Resource
import json

lista_habilidades = ['Python', 'Java', 'Flask', 'Python', 'PHP', 'UX', 'JavaScript']
class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)
        posicao = len(lista_habilidades)
        dados['id'] = posicao
        lista_habilidades.append(dados)
        return lista_habilidades[posicao]

    def put(self, id):
        dados = json.loads(request.data)
        if id < len(lista_habilidades):
            lista_habilidades[id] = dados
            return dados
        else:
            return {'mensagem':'ID de habilidade inválido'}, 404 #not found

    def delete(self, id):
        if id < len(lista_habilidades):
            habilidade_removida = lista_habilidades.pop(id)
            return {'status':'sucesso', 'mensagem':'Registro excluído'}
        else:
            return {'mensagem':'ID de habilidade inválido'}, 404


