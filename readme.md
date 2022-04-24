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

* validacao de dados de entrada
* explicacao de qual backend usou para as tarefas como um comparativo entre outros
* resolucao de erros de codigo
* rotas RESTFULL
* documentacao do codigo via fastapi
* configuracao dinamica das variaveis de configuracao do servidor
* criacao de um dockerfile do servidor e respectivos backends caso tenha
* adicionar autenticacao APENAS nas rotas de tarefas(usando x-apikey, pode deixar apikey hardcoded)
* criar um handling de erro customizado para voltar no request o erro(explicacao traceback)
* criar uma rota de health
* criacao de testes unitarios
* lint