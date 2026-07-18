class ObjectTracker:

    def __init__(self, model):
        self.model = model

    def track(self, frame, confidence_threshold):
        results = self.model.track(
            frame,
            persist=True,
            conf=confidence_threshold,
            tracker="bytetrack.yaml",
            verbose=False
        )

        return results