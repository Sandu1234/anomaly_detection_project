import numpy as np
import time

def data_stream():
    while True:
        base = np.sin(time.time()) * 10  # Simulate a regular pattern
        noise = np.random.normal(0, 2)  # Add some random noise
        anomaly = np.random.choice([0, 1], p=[0.99, 0.01])  # 1% chance of anomaly
        value = base + noise + (anomaly * np.random.randint(50, 100))  # Anomalous value if anomaly occurs
        yield value
        time.sleep(1)  # Wait for 1 second to simulate real-time data stream
