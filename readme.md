## Teste de Backend PSAFE

### Como executar o projeto

Crie um ambiente virtual python, preferencialmente na versão 3.8.10

Instale as dependencias necessarias com:

```pip install -r requirements.txt```

```python run.py```

### Como executar o projeto em um container docker
 
Necessário que tenha o docker devidamente instalado e configurado. Dois comandos são necessários, primeiro
para buildar a imagem docker e em seguida para subir um container com essa imagem.

```sudo docker build -t tasks .```

```docker run -d --name tasks_container -p 8081:8081 tasks```

Estará rodando em localhost:8081/

### Testes unitários e Lint

Para executar os testes e o lint é necessario instalar tox e pylint.
```pip install tox```

```pip install pylint```

Testes unitarios foram implementados para as 3 novas rotas estão organizado em tests/conftest.py e tasks_test.py.
Para rodar somente os testes unitarios use:

```tox -e unit```

Para executar somente a verificação com lint, use:
```tox -e lint```

Para executar os dois, use:
```tox```


### Documentação das rotas

Com server rodando acesse pelo navegador localhost:8081/docs

### Observações
- As rotas das Tasks são protegidas por x-apikey, é necessario passa a key nesse campo.
A key padrão é ```a7f9fa60-992d-4fb9-9f53-e8b1981ad418```. Mas você pode definir outra key, setando
a variavel de ambiente harded_apikey.


- Todo o desenvolvimento do teste foi utilizado em memoria, ou seja, ao reiniciar a aplicação todos os estados de Tasks serão perdidos.