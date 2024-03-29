Projeto Flask de Gerenciamento de Desenvolvedores e Habilidades
Este é um projeto Flask que oferece uma API para gerenciar informações sobre desenvolvedores e suas habilidades. Ele fornece endpoints para listar, adicionar, atualizar e excluir desenvolvedores, bem como para gerenciar habilidades.

Funcionalidades
Desenvolvedores:

Listar todos os desenvolvedores
Obter informações de um desenvolvedor específico por ID
Adicionar um novo desenvolvedor
Atualizar informações de um desenvolvedor existente
Excluir um desenvolvedor
Habilidades:

Listar todas as habilidades
Obter informações de uma habilidade específica por ID
Adicionar uma nova habilidade
Atualizar informações de uma habilidade existente
Excluir uma habilidade
Como Usar
Instale as dependências necessárias do Python listadas no arquivo requirements.txt usando pip:

pip install -r requirements.txt
Execute o arquivo app.py para iniciar o servidor Flask:

python app_restful.py
A API estará disponível em http://localhost:5000/. Você pode acessar os endpoints utilizando ferramentas como Postman.

Endpoints
GET /dev/: Lista todos os desenvolvedores.
POST /dev/: Adiciona um novo desenvolvedor.
GET /dev/<id>/: Obtém informações de um desenvolvedor específico por ID.
PUT /dev/<id>/: Atualiza informações de um desenvolvedor existente por ID.
DELETE /dev/<id>/: Exclui um desenvolvedor existente por ID.
GET /habilidades/: Lista todas as habilidades.
POST /habilidades/: Adiciona uma nova habilidade.
GET /habilidades/<id>/: Obtém informações de uma habilidade específica por ID.
PUT /habilidades/<id>/: Atualiza informações de uma habilidade existente por ID.
DELETE /habilidades/<id>/: Exclui uma habilidade existente por ID.
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar pull requests com melhorias, correções de bugs ou novos recursos.
