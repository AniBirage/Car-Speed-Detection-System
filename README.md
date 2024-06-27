# Car-Speed-Detection-System

This project aims to detect the speed of cars in a video using a pre-trained SSD (Single Shot Multibox Detector) model and issue speeding tickets if the detected speed exceeds a specified limit.

## Files

- **Test.py**: This script loads a video file and prints the frame rate of the video.
- **CarSpeedDetection(SSD).py**: This script contains the main logic for detecting car speeds, drawing bounding boxes around detected cars, calculating their speeds, and issuing speeding tickets.
- **Cars.mp4**: A sample video file containing footage of cars.
- **SpeedingTicket.txt**: A file where speeding tickets are recorded with the detected speed and the fine amount.

## Prerequisites

- Python 3.6 or higher
- OpenCV
- PyTorch
- torchvision
- numpy

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/AniBirage/Car-Speed-Detection-System.git
    cd Car-Speed-Detection-System\Car_Speed_Detection_System
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run `Test.py` to verify that the video file can be loaded and to print the frame rate:
    ```bash
    python Test.py
    ```

2. Run `CarSpeedDetection(SSD).py` to start detecting car speeds and issuing speeding tickets:
    ```bash
    python CarSpeedDetection(SSD).py
    ```

3. During the execution of `CarSpeedDetection(SSD).py`, a window will display the video with detected cars and their speeds. If a car's speed exceeds the speed limit, a speeding ticket will be issued and saved in `SpeedingTicket.txt`.

4. Press `q` to quit the video window.

## Configuration

- `conf_threshold`: Confidence threshold for detecting cars. Default is `0.5`.
- `frame_rate`: Frame rate of the video. Default is `12.0`.
- `ppm`: Pixels per meter. Default is `8.8`.
- `speed_limit`: Speed limit in km/h. Default is `3744` km/h.
- `fine`: Fine amount for speeding. Default is `$25`.

You can adjust these values in the `CarSpeedDetection(SSD).py` file according to your requirements.

## Acknowledgments

This project uses the following libraries and resources:

- [OpenCV](https://opencv.org/)
- [NumPy](https://numpy.org/)
- [PyTorch](https://pytorch.org/)

Feel free to contribute to this project by creating pull requests or reporting issues.
