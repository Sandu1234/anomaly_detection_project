Efficient Data Stream Anomaly Detection

Overview

This project is part of an application for the Graduate Software Engineer role at Cobblestone Energy. It implements a Python script to detect anomalies in a continuous data stream. The data stream simulates real-time sequences of floating-point numbers, representing various metrics such as financial transactions or system performance.

The goal is to identify unusual patterns, such as exceptionally high values or deviations from the normal data flow, using a real-time anomaly detection algorithm.

Algorithm

We use the Z-Score anomaly detection algorithm. The Z-Score measures how many standard deviations a data point is from the mean of a sliding window of recent data points. If the Z-Score exceeds a predefined threshold, the data point is flagged as an anomaly.

Window Size: The sliding window holds the most recent data points, and this size is configurable.
Threshold: A threshold Z-Score is used to determine if a point is anomalous (e.g., any data point with a Z-Score > 3 is flagged).

Data Simulation

The data stream consists of:

A regular sinusoidal pattern (using the sine function to represent periodic changes).
Random noise added to simulate fluctuations.
Occasionally, anomalies are introduced (large deviations from the normal pattern).

Error Handling and Data Validation

To handle potential issues in a real-time data stream, the project includes:

Data validation: Each data point is checked to ensure it is a valid numeric value.
Error handling: Invalid or missing data points (e.g., None values) are skipped, and errors are logged without crashing the program.
A 5% chance of generating an invalid data point (None) is intentionally introduced to test the system's robustness.

Project Structure

data_stream.py: Simulates the real-time data stream with regular patterns, random noise, and anomalies. Includes error handling for invalid data points.
anomaly_detector.py: Implements the Z-Score anomaly detection algorithm using a sliding window and detects whether new data points are anomalous.
main.py: Integrates the data stream and anomaly detection, and visualizes the data in real-time using matplotlib. Detected anomalies are highlighted in red on the graph.

How to Run the Project

Requirements

Python 3.x
Installation
Clone or download the project files to your local machine.
Navigate to the project directory.
Install the required libraries by running the following command:

pip install -r requirements.txt

Running the Project

To run the anomaly detection and visualization:

python main.py

This will start simulating the real-time data stream, detecting anomalies, and plotting the results.

Visualization

The visualization shows:

Blue line: Represents the data stream with regular and noisy data.
Red dots: Highlight data points that have been flagged as anomalies by the Z-Score detector.
The script continues running in real-time, plotting each new data point and detecting anomalies as they occur.

Error Handling and Data Validation

This project includes robust error handling to ensure that invalid data points do not crash the program:

If a None value or non-numeric data is encountered, the system logs the error (Invalid data point) and skips that data point, allowing the program to continue running smoothly.
Standard deviation of zero (which could lead to a division-by-zero error) is also caught and handled, ensuring that the anomaly detection remains stable.

External Libraries

NumPy: For numerical operations and generating data.
Matplotlib: For real-time visualization of the data stream and detected anomalies.

These libraries are listed in the requirements.txt file for easy installation.

Conclusion

This project demonstrates the real-time detection of anomalies in a continuous data stream using the Z-Score method. The system is designed to be robust, handling invalid or missing data points gracefully, while efficiently detecting and flagging unusual patterns in the data.