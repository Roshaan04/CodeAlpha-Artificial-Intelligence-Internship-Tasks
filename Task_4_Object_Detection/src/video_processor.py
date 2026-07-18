import cv2
import time


class VideoProcessor:

    def __init__(self, tracker, confidence_threshold):
        self.tracker = tracker
        self.confidence_threshold = confidence_threshold

    def run(self, source=0):

        cap = cv2.VideoCapture(source)

        if not cap.isOpened():
            print("Error: Could not open video source.")
            return

        previous_time = 0

        while True:

            success, frame = cap.read()

            if not success:
                print("Error: Could not read frame.")
                break

            results = self.tracker.track(
                frame,
                self.confidence_threshold
            )

            annotated_frame = results[0].plot()

            current_time = time.time()

            fps = 1 / (current_time - previous_time) \
                if previous_time != 0 else 0

            previous_time = current_time

            cv2.putText(
                annotated_frame,
                f"FPS: {fps:.2f}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            cv2.imshow(
                "AI Object Detection and Tracking",
                annotated_frame
            )

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()