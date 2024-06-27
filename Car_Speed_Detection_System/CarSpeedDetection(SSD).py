import numpy as np
import cv2
import torch
import torchvision as tv
import math
import time

model = tv.models.detection.ssdlite320_mobilenet_v3_large(pretrained=True)
model.eval()

conf_threshold = 0.5
frame_rate = 12.0
ppm = 8.8
speed_limit = 3744
fine = 25


def detect_speed(l1, l2, ppm, fps):
    d_pixel = math.sqrt((l2[0] - l1[0]) ** 2 + (l2[1] - l1[1]) ** 2)
    d_metre = d_pixel / ppm
    speed = d_metre * fps * 3.6
    return speed


def detect_cars(frame, frame_rate, ppm):
    global pos_list_prev
    image_tensor = tv.transforms.ToTensor()(frame)
    with torch.no_grad():
        predictions = model([image_tensor])
    for pred, score in zip(predictions[0]["boxes"], predictions[0]["scores"]):
        x1, y1, x2, y2 = map(int, pred)
        if score >= conf_threshold:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cent_x = (x1 + x2) / 2
            cent_y = (y1 + y2) / 2
            post_list = [cent_x, cent_y]
            if pos_list_prev is not None:
                speed = detect_speed(pos_list_prev, post_list, ppm, frame_rate)
                if speed >= speed_limit:
                    issue_speeding_ticket(speed)
                    print("Speeding Ticket Issued")
            else:
                speed = 0
            cv2.putText(
                frame,
                f"Speed:{speed:.2f} km/h",
                (x1, y1 + 20),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2,
            )
            pos_list_prev = post_list
    return frame


def issue_speeding_ticket(speed):
    filename = "SpeedingTicket.txt"
    with open(filename, "a") as file:
        file.write("Speeding Ticket!\n")
        file.write(f"Detected Speed:{speed:.2f} km/h\n")
        file.write(f"Fine Amount:${fine}\n")
        file.write("\n")


cap = cv2.VideoCapture("Cars.mp4")

if not cap.isOpened():
    print(" Error! Unable to Load Video")
    exit()

pos_list_prev = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    process_frame = detect_cars(frame, frame_rate, ppm)
    cv2.imshow("Cars With Speed", process_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
