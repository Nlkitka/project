import pika
import json


def send_mes(mes_body: dict):
    """
    the function passes to the queue called "post_add_result" a dictionary with the key post id and the value ad/not ad
    :param mes_body: dictionary
    :return:
    """
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        'localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='post_add_result')
    user_encode_data = json.dumps(mes_body, indent=2).encode('utf-8')
    print(user_encode_data)
    channel.basic_publish(exchange='',
                          routing_key='post_add_result',
                          body=user_encode_data)
    print(" [x] Sent 'post's ids with info'")
    connection.close()
