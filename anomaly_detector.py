from collections import deque
import numpy as np

class ZScoreAnomalyDetector:
    def __init__(self, window_size, threshold):
        self.window_size = window_size
        self.threshold = threshold
        self.data = deque(maxlen=window_size)  # Store recent values

    def detect(self, new_value):
        self.data.append(new_value)
        if len(self.data) == self.window_size:
            mean = np.mean(self.data)
            std = np.std(self.data)
            z_score = (new_value - mean) / std
            return abs(z_score) > self.threshold  # Flag as anomaly if z-score is beyond threshold
        return False
