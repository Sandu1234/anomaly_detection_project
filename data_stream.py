import numpy as np
import time

# Helper function to validate data
def is_valid_data_point(value):
    """Check if the data point is a valid numeric value."""
    if value is None or not isinstance(value, (int, float)):
        return False
    return True

def data_stream():
    while True:
        try:
            base = np.sin(time.time()) * 10  # Simulate regular pattern
            noise = np.random.normal(0, 2)  # Add random noise
            anomaly = np.random.choice([0, 1], p=[0.99, 0.01])  # 1% chance of anomaly
            value = base + noise + (anomaly * np.random.randint(50, 100))  # Introduce anomaly if it occurs
            
            # Introduce an invalid data point with 5% probability
            if np.random.rand() < 0.05:  # 5% chance of introducing invalid data
                value = None  # Introduce a None value (invalid data)
            
            # Validate the data point before yielding
            if not is_valid_data_point(value):
                raise ValueError(f"Invalid data point: {value}")
            
            yield value

        except ValueError as ve:
            print(f"Error generating data point: {ve}")  # Handle specific data validation errors
        except Exception as e:
            print(f"An unexpected error occurred: {e}")  # Catch any other unexpected errors
        finally:
            time.sleep(1)  # Simulate real-time data stream
