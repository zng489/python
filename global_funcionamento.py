import json
import logging
import os
import shutil
import subprocess
import sys
import threading
import time
import uuid
from datetime import date, datetime
from pathlib import Path

import pika
from dotenv import load_dotenv, find_dotenv

# Módulos internos do projeto
from etl.pipelines.base_pipelines import pipelines
from _logging.logger import configurar_logger
from etl.pipelines.pipelines_run import *


load_dotenv(find_dotenv())

logger = configurar_logger("[o] rabbitmq_consumer.py - ") 
threadRunning = False

versao_json = None

# Função para manter a conexão com o RabbitMQ ativa
# (precisa chamar process_data_events periodicamente)
def heartbeat(connection) -> None:
    global threadRunning

    while True:
        if not threadRunning:
            break
        connection.process_data_events()
        time.sleep(30)


def callback(ch, method, properties, body):
    try:
        message = json.loads(body)
        #time.sleep(3)
        #logger.info("[OK] ")

        print(message)

        # Rodando pipeline após receber a mensagem
        pipeline = run_pipeline(message['id'], versao_json )
        pipeline.run()


        # Confirma recebimento da mensagem
        ch.basic_ack(method.delivery_tag, False)
        logger.info("Mensagem processada com sucesso")
        
    except Exception as e:
        logger.error(f"[X] Erro ao processar mensagem: {e}")
        import traceback
        logger.error(traceback.format_exc())

        ch.basic_nack(method.delivery_tag, False, True)
        

def iniciar_consumidor():
    global versao_json
    try:

        with open("modelos/modelo_atual.json", "r") as f:
            modelo = json.load(f)
            versao_json = modelo["versao"]

        conn_mq = {
            "user": os.getenv("RABBITMQ_USERNAME"),
            "passwd": os.getenv("RABBITMQ_PASSWORD"),
            "host": os.getenv("RABBITMQ_HOST"),
            "vhost": os.getenv("RABBITMQ_VHOST"),
            "port": int(os.getenv("RABBITMQ_PORT")),
            "exchange": os.getenv("RABBITMQ_EXCHANGE") or '',
            "routing_key": os.getenv("RABBITMQ_ROUTING_KEY"),
            "queue": os.getenv("RABBITMQ_QUEUE")
        }
        cred = pika.PlainCredentials(conn_mq["user"], conn_mq["passwd"])
        params = pika.ConnectionParameters(
            host=conn_mq["host"],
            virtual_host=conn_mq["vhost"],
            port=conn_mq["port"],
            credentials=cred,
            heartbeat=60,  # ou menor, como 30
            blocked_connection_timeout=300
        )

        logger.info("Conectando ao RabbitMQ...")
        connection = pika.BlockingConnection(params)
        channel = connection.channel()

        # Declara novamente para garantir que a fila existe
        #channel.queue_declare(queue=conn_mq["queue"], durable=True, arguments={"x-queue-type": "quorum"})

        # Inicia consumo

        thread = threading.Thread(target=heartbeat, args=(connection,))
        threadRunning = True
        thread.start()

        logger.info("[O] Esperando mensagens. Pressione CTRL+C para sair.")
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=conn_mq["queue"], on_message_callback=callback, auto_ack=False)

        channel.start_consuming()

    except KeyboardInterrupt:
        logger.info("[X] Interrompido pelo usuário.")
    except Exception as e:
        logger.error(f"[X] Erro geral: {e}")
        import traceback
        logger.error(traceback.format_exc())


