https://www.rabbitmq.com/tutorials/tutorial-one-python.html

Nosso primeiro programa send.py enviará uma única mensagem para a fila. A primeira coisa que precisamos fazer é estabelecer uma conexão com o servidor RabbitMQ.

Requisito:

Deve ter subido o servidor com os comandos:

```s
docker pull rabbitmq:3.9-management
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9-management
```

Estamos conectados agora, a um broker na máquina local - daí o localhost . Se quisermos nos conectar a um broker em uma máquina diferente, basta especificar seu nome ou endereço IP aqui.

Em seguida, antes de enviar, precisamos garantir que a fila de destinatários exista. Se enviarmos uma mensagem para um local não existente, o RabbitMQ apenas descartará a mensagem. Vamos criar uma fila hello para a qual a mensagem será entregue:

# Subindo o Container do RabbitMQ e Rodando Producer e Consumer manualmente

```s
cd docker/05-rabbitmq-only
docker-compose -f 05-docker-compose-rabbitmq.yml up -d
```

Inicialize o ambiente:

```s
poetry shell
```

Instale os packages:
```s
poetry install
```

Execute o `consumer.py` em um terminal:

```s
python consumer.py
```

Execute o `producer.py` em outro terminal:

```s
python producer.py
```

Ao voltar no terminal do Consumer você deverá ver:

```s
python consumer.py
 [*] Connecting to server ...
 [*] Waiting for messages. To exit press Ctrl+C
 [x] Recebida a mensagem b'iniciar'
Chamando inicia_contagem()
count: 1
count: 2
count: 3
count: 4
count: 5
count: 6
count: 7
count: 8
count: 9
```


# Subindo os Containers com Traefik - Local

Nome da rede que vamos utilizar:

```s
docker network create web
```

Suba o Traefik - Proxy Reverso com o comando:

```s
cd docker/01-traefik
docker-compose -f 01-docker-compose-traefik-local.yml up -d
```

Acesse http://localhost:8080/

Depois suba o container do RabbitMQ:

```s
cd docker/02-rabbitmq-traefik
docker-compose -f 02-docker-compose-rabbitmq.yml up -d
```

Acesse http://localhost:15672/
com login e senha: guest

Suba o container do Consumer e do Producer.

Lembrando que o Producer está programado para executar uma só vez.
