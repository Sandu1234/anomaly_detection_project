from collections import deque
import numpy as np
from data_stream import is_valid_data_point  # Import the helper function

class ZScoreAnomalyDetector:
    def __init__(self, window_size, threshold):
        self.window_size = window_size
        self.threshold = threshold
        self.data = deque(maxlen=window_size)  # Store recent values

    def detect(self, new_value):
        try:
            # Validate the new data point
            if not is_valid_data_point(new_value):
                raise ValueError(f"Invalid data point: {new_value}")

            self.data.append(new_value)

            if len(self.data) == self.window_size:
                mean = np.mean(self.data)
                std = np.std(self.data)

                if std == 0:  # Prevent division by zero
                    raise ZeroDivisionError("Standard deviation is zero. Can't compute Z-score.")

                z_score = (new_value - mean) / std
                return abs(z_score) > self.threshold  # Return True if anomaly is detected

            return False  # No anomaly if the window isn't full yet

        except ZeroDivisionError as zde:
            print(f"Error during anomaly detection: {zde}")
            return False  # Treat as no anomaly if there's an error
        except ValueError as ve:
            print(f"Error: {ve}")
            return False  # Treat as no anomaly if there's an invalid data point
        except Exception as e:
            print(f"Unexpected error during anomaly detection: {e}")
            return False  # Treat as no anomaly if there's an unexpected error
