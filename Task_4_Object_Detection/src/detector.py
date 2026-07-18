from ultralytics import YOLO


class ObjectDetector:

    def __init__(self, model_path, confidence_threshold):
        self.model = YOLO(model_path)
        self.confidence_threshold = confidence_threshold

    def detect(self, frame):
        results = self.model(
            frame,
            conf=self.confidence_threshold,
            verbose=False
        )

        return results