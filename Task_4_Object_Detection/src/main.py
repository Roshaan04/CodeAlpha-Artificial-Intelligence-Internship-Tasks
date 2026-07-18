from config import (
    MODEL_PATH,
    CONFIDENCE_THRESHOLD,
    SOURCE
)

from detector import ObjectDetector
from tracker import ObjectTracker
from video_processor import VideoProcessor


def main():

    print("Starting AI Object Detection and Tracking System...")

    detector = ObjectDetector(
        MODEL_PATH,
        CONFIDENCE_THRESHOLD
    )

    tracker = ObjectTracker(
        detector.model
    )

    video_processor = VideoProcessor(
        tracker,
        CONFIDENCE_THRESHOLD
    )

    video_processor.run(SOURCE)


if __name__ == "__main__":
    main()
