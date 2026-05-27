from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

import cv2

# -----------------------------------
# LOAD YOLO MODEL
# -----------------------------------
model = YOLO("yolov8n.pt")

# -----------------------------------
# INITIALIZE DEEPSORT TRACKER
# -----------------------------------
tracker = DeepSort(
    max_age=30
)

# -----------------------------------
# STORE UNIQUE IDS
# -----------------------------------
unique_track_ids = set()

# -----------------------------------
# OPEN WEBCAM
# -----------------------------------
cap = cv2.VideoCapture(0)

print("Press Q to quit")

# -----------------------------------
# MAIN LOOP
# -----------------------------------
while True:

    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    # -------------------------------
    # YOLO DETECTION
    # -------------------------------
    results = model(frame)

    detections = []

    # -------------------------------
    # EXTRACT DETECTIONS
    # -------------------------------
    for result in results:

        boxes = result.boxes

        for box in boxes:

            x1, y1, x2, y2 = box.xyxy[0]

            confidence = box.conf[0].item()

            class_id = int(box.cls[0].item())

            # Only PERSON class
            if class_id == 0:

                width = x2.item() - x1.item()
                height = y2.item() - y1.item()

                detections.append(
                    (
                        [
                            x1.item(),
                            y1.item(),
                            width,
                            height
                        ],
                        confidence,
                        "person"
                    )
                )

    # -------------------------------
    # UPDATE TRACKER
    # -------------------------------
    tracks = tracker.update_tracks(
        detections,
        frame=frame
    )

    # -------------------------------
    # DRAW TRACKS
    # -------------------------------
    for track in tracks:

        if not track.is_confirmed():
            continue

        track_id = track.track_id

        # Add ID to set
        unique_track_ids.add(track_id)

        ltrb = track.to_ltrb()

        x1, y1, x2, y2 = map(int, ltrb)

        # Draw rectangle
        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        # Draw tracking ID
        cv2.putText(
            frame,
            f"ID: {track_id}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    # -------------------------------
    # DISPLAY PEOPLE COUNT
    # -------------------------------
    people_count = len(unique_track_ids)

    cv2.putText(
        frame,
        f"People Count: {people_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        3
    )

    # -------------------------------
    # SHOW OUTPUT
    # -------------------------------
    cv2.imshow(
        "Smart Surveillance System",
        frame
    )

    # -------------------------------
    # EXIT
    # -------------------------------
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# -----------------------------------
# CLEANUP
# -----------------------------------
cap.release()

cv2.destroyAllWindows()