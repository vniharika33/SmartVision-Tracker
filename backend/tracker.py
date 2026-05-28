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
# VIDEO PROCESSING FUNCTION
# -----------------------------------
def process_video(input_path, output_path):

    # Open input video
    cap = cv2.VideoCapture(input_path)

    # Video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Output video writer
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    out = cv2.VideoWriter(
        output_path,
        fourcc,
        fps,
        (width, height)
    )

    # -----------------------------------
    # MAIN LOOP
    # -----------------------------------
    while True:

        ret, frame = cap.read()

        if not ret:
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

                # PERSON CLASS ONLY
                if class_id == 0:

                    width_box = x2.item() - x1.item()
                    height_box = y2.item() - y1.item()

                    detections.append(
                        (
                            [
                                x1.item(),
                                y1.item(),
                                width_box,
                                height_box
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
        # STORE ACTIVE TRACK IDs
        # -------------------------------
        active_track_ids = set()

        # -------------------------------
        # DRAW TRACKS
        # -------------------------------
        for track in tracks:

            # Ignore unconfirmed tracks
            if not track.is_confirmed():
                continue

            # Unique ID
            track_id = track.track_id

            # Store ACTIVE ID only
            active_track_ids.add(track_id)

            # Bounding box
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

            # Draw ID label
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
        # PEOPLE COUNT
        # -------------------------------
        people_count = len(active_track_ids)

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
        # WRITE OUTPUT FRAME
        # -------------------------------
        out.write(frame)

    # -----------------------------------
    # CLEANUP
    # -----------------------------------
    cap.release()

    out.release()

    print("Video processing completed!")