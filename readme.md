## Teste de Backend PSAFE

### Modifique o servico em FastApi adicionando as seguintes 3 rotas:

#### /add_task

Cria uma tarefa assíncrona e retorna um id único desta tarefa.

Essa tarefa assíncrona contém apenas um sleep de 10 segundos

#### /count

Retorna o total de tarefas em andamento

#### /query

Recebe um id de tarefa via GET ou POST, e retorna o status da tarefa:

* não encontrado
* rodando
* concluído


### Observacoes
* Voce pode usar qualquer metodo para organizar as tarefas, sera levado em conta
o por que de voce ter escolhido o metodo.
* Para rodar o Servico voce precisara executar o arquivo run.py, o servidor esta subindo porem
com alguns erros


### Adicionais
Existem muitas melhorias neste projeto, para verificar senioridade e diferencial, alem das rotas base
sugerimos alguns adicionais para este projeto

* validacao de dados de entrada - ok
* explicacao de qual backend usou para as tarefas como um comparativo entre outros
* resolucao de erros de codigo - ok
* rotas RESTFULL - ok
* documentacao do codigo via fastapi - todo
* configuracao dinamica das variaveis de configuracao do servidor - todo
* criacao de um dockerfile do servidor e respectivos backends caso tenha - todo
* adicionar autenticacao APENAS nas rotas de tarefas(usando x-apikey, pode deixar apikey hardcoded) - todo
* criar um handling de erro customizado para voltar no request o erro(explicacao traceback) - todo
* criar uma rota de health - todo
* criacao de testes unitarios - todo
* lint - todo



sudo docker build -t tasks .

docker run -d --name tas -p 8081:8081 tasks



export harded_apikey="a7f9fa60-992d-4fb9-9f53-e8b1981ad418"
export app_title="Dev Tasks Teste"
export app_description="Test backend developer PSafe"
export app_version="0.0.0.1"