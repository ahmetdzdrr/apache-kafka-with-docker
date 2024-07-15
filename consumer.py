from kafka import KafkaConsumer
import json
import threading

consumer = KafkaConsumer('topic3', 
                         bootstrap_servers='localhost:9092',
                         auto_offset_reset='earliest',
                         group_id='my-group', 
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

output_file = 'data.json'
duration = 30 

data = []

def consumer_message():
    global data
    consumer.close()
    print("Consumer has been stopped.")
    # Write data to JSON file after stopping the consumer
    try:
        with open(output_file, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data written to {output_file}")
    except Exception as e:
        print(f"An error occurred while writing to {output_file}: {e}")

# Start a timer to stop the consumer after the duration
timer = threading.Timer(duration, consumer_message)
timer.start()

try:
    for message in consumer:
        message_value = message.value
        print(f"Received message: {message_value}\n")
        data.append(message_value)
except KeyboardInterrupt:
    print("Process interrupted by the user.")
    consumer_message()
finally:
    if not consumer.closed:
        consumer_message()
