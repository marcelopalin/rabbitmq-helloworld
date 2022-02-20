"""
    Description:

    Consumer - fica lendo a fila do RabbitMQ
    se recebe uma mensagem com a palavra iniciar
    inicia uma contagem até 10.

    Author:           @Palin
    Created:          2022-02-18
"""


try:
    import os
    import sys
    import time
    from pathlib import Path

    import pika
except ImportError as error:
    print(error)
    print(f"error.name: {error.name}")
    print(f"error.path: {error.path}")


def inicia_contagem():
    for i in range(1, 10):
        print(f"count: {i}")
        time.sleep(1)


def on_message(channel, method, properties, body):
    print(f" [x] Recebida a mensagem {body}")
    if "iniciar" in body.decode("ascii"):
        print("Chamando inicia_contagem()")
        inicia_contagem()
    else:
        print("Nada a ser feito!")
    channel.basic_ack(delivery_tag=method.delivery_tag)


def main():

    # Caso suba com docker este script utilize
    # SERVER = "rabbitmq"

    SERVER = "localhost"
    FILA = "task_queue"
    print(" [*] Connecting to server ...")
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=SERVER))
    channel = connection.channel()
    channel.queue_declare(queue=FILA)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=FILA, on_message_callback=on_message)

    try:
        print(" [*] Waiting for messages. To exit press Ctrl+C")
        channel.start_consuming()
    except KeyboardInterrupt:
        print(" [x] Done")


if __name__ == "__main__":
    main()
