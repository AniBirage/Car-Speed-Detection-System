import cv2

cap = cv2.VideoCapture("Cars.mp4")

if not cap.isOpened():
    print("Error! Unable to Load Video")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
print(f"Frame Rate:{fps}")
cap.release()
