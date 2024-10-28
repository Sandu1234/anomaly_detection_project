import matplotlib.pyplot as plt
from data_stream import data_stream, is_valid_data_point  # Import helper function
from anomaly_detector import ZScoreAnomalyDetector

def visualize(stream, detector):
    data_points = []
    anomalies = []

    plt.ion()  # Interactive mode on
    fig, ax = plt.subplots()

    for point in stream:
        try:
            # Validate data point
            if not is_valid_data_point(point):
                raise ValueError(f"Invalid data point received: {point}")

            data_points.append(point)
            anomaly = detector.detect(point)
            anomalies.append(anomaly)

            # Clear the plot and re-plot updated data
            ax.clear()
            ax.plot(data_points, label='Data Stream')

            # Highlight anomalies in red
            anomaly_points = [p if a else None for p, a in zip(data_points, anomalies)]
            ax.scatter(range(len(data_points)), anomaly_points, color='r', label='Anomaly')

            ax.legend()
            plt.pause(0.05)  # Pause for 50ms to simulate real-time updates

        except ValueError as ve:
            print(f"Data error: {ve}")
        except Exception as e:
            print(f"Unexpected error during visualization: {e}")
            break  # Break the loop on unexpected error

if __name__ == "__main__":
    detector = ZScoreAnomalyDetector(window_size=50, threshold=3)  # Initialize the detector
    stream = data_stream()  # Get the simulated data stream
    visualize(stream, detector)  # Start visualizing
