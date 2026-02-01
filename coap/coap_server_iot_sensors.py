"""
CoAP IoT Server – Normal Traffic Generation
This server simulates multiple IoT sensors using CoAP protocol.
Used to generate legitimate traffic for intrusion detection experiments.
"""

from coapthon.server.coap import CoAP
from coapthon.resources.resource import Resource
import random

# --- Capteurs personnalisés ---
class TemperatureResource(Resource):
    def __init__(self, name="temperature", coap_server=None):
        super().__init__(name, coap_server)
        self.payload = self.generate()

    def render_GET(self, request):
        self.payload = self.generate()
        return self

    def generate(self):
        return f"{random.uniform(36.0, 38.0):.2f}°C"

class HumidityResource(Resource):
    def __init__(self, name="humidity", coap_server=None):
        super().__init__(name, coap_server)
        self.payload = self.generate()

    def render_GET(self, request):
        self.payload = self.generate()
        return self

    def generate(self):
        return f"{random.uniform(40.0, 70.0):.2f}%"

class OxygenResource(Resource):
    def __init__(self, name="oxygen", coap_server=None):
        super().__init__(name, coap_server)
        self.payload = self.generate()

    def render_GET(self, request):
        self.payload = self.generate()
        return self

    def generate(self):
        return f"{random.uniform(95.0, 100.0):.1f}%"

class BarometerResource(Resource):
    def __init__(self, name="barometer", coap_server=None):
        super().__init__(name, coap_server)
        self.payload = self.generate()

    def render_GET(self, request):
        self.payload = self.generate()
        return self

    def generate(self):
        return f"{random.uniform(980, 1050):.1f} hPa"

class ECGResource(Resource):
    def __init__(self, name="ecg", coap_server=None):
        super().__init__(name, coap_server)
        self.payload = self.generate()

    def render_GET(self, request):
        self.payload = self.generate()
        return self

    def generate(self):
        return f"{random.randint(60, 100)} bpm"

class NasalResource(Resource):  # Airflow sensor
    def __init__(self, name="nasal", coap_server=None):
        super().__init__(name, coap_server)
        self.payload = self.generate()

    def render_GET(self, request):
        self.payload = self.generate()
        return self

    def generate(self):
        return f"{random.uniform(5.0, 20.0):.1f} L/min"

class GlucometerResource(Resource):
    def __init__(self, name="glucometer", coap_server=None):
        super().__init__(name, coap_server)
        self.payload = self.generate()

    def render_GET(self, request):
        self.payload = self.generate()
        return self

    def generate(self):
        return f"{random.randint(70, 140)} mg/dL"

class PressureResource(Resource):  # Blood pressure
    def __init__(self, name="pressure", coap_server=None):
        super().__init__(name, coap_server)
        self.payload = self.generate()

    def render_GET(self, request):
        self.payload = self.generate()
        return self

    def generate(self):
        return f"{random.randint(100, 140)}/{random.randint(60, 90)} mmHg"

class BodyResource(Resource):  # Body temperature
    def __init__(self, name="body", coap_server=None):
        super().__init__(name, coap_server)
        self.payload = self.generate()

    def render_GET(self, request):
        self.payload = self.generate()
        return self

    def generate(self):
        return f"{random.uniform(36.0, 37.5):.2f}°C"

# --- Lancer le serveur ---
server = CoAP(("127.0.0.1", 5683))
server.add_resource("temperature/", TemperatureResource("temperature"))
server.add_resource("humidity/", HumidityResource("humidity"))
server.add_resource("oxygen/", OxygenResource("oxygen"))
server.add_resource("barometer/", BarometerResource("barometer"))
server.add_resource("ecg/", ECGResource("ecg"))
server.add_resource("nasal/", NasalResource("nasal"))
server.add_resource("glucometer/", GlucometerResource("glucometer"))
server.add_resource("pressure/", PressureResource("pressure"))
server.add_resource("body/", BodyResource("body"))

print("✅ CoAP Server is running on 127.0.0.1:5683 with all IoT-Flock resources.")
print(server.root.dump())
server.listen(10)
