import pika


def main():

    """Nesta parte do tutorial vamos escrever dois pequenos programas
    em Python; um produtor (remetente) que envia uma única mensagem e
    um consumidor (receptor) que recebe as mensagens e as imprime.
    É um "Hello World" de mensagens.
    """
    # Caso suba com docker este script utilize
    # SERVER = "rabbitmq"

    SERVER = "localhost"
    FILA = "task_queue"
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=SERVER))
    channel = connection.channel()

    # Cria uma fila
    channel.queue_declare(queue=FILA)

    # No RabbitMQ uma mensagem nunca pode ser enviada diretamente para a fila,
    # ela sempre precisa passar por uma Exchange (troca)
    # Tudo o que precisamos saber agora é como usar uma troca padrão identificada por
    # uma string vazia. Essa troca é especial – ela nos permite especificar
    # exatamente para qual fila a mensagem deve ir. O nome da fila precisa
    # ser especificado no parâmetro routing_key :
    msg = f"iniciar"
    channel.basic_publish(exchange="", routing_key=FILA, body=msg)
    print(f" [x] Enviando a mensagem {msg}")
    connection.close()


if __name__ == "__main__":
    main()
