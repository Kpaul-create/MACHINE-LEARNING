import cv2
import mediapipe as mp
import time
import numpy as np
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Constants
MODEL_PATH = 'efficientdet_lite0.tflite'

def visualize(image, detection_result):
    """Draws bounding boxes on the input image and return it."""
    for detection in detection_result.detections:
        # Draw bounding_box
        bbox = detection.bounding_box
        start_point = (bbox.origin_x, bbox.origin_y)
        end_point = (bbox.origin_x + bbox.width, bbox.origin_y + bbox.height)
        cv2.rectangle(image, start_point, end_point, (0, 255, 0), 3)

        # Draw label and score
        category = detection.categories[0]
        category_name = category.category_name
        probability = round(category.score, 2)
        result_text = f'{category_name} ({probability})'
        text_location = (bbox.origin_x, bbox.origin_y - 10)
        cv2.putText(image, result_text, text_location, cv2.FONT_HERSHEY_SIMPLEX, 
                    1, (0, 255, 0), 2, cv2.LINE_AA)
    return image

def main():
    print("Initializing MediaPipe Object Detector...")
    
    # Create an ObjectDetector object.
    base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
    options = vision.ObjectDetectorOptions(base_options=base_options,
                                           running_mode=vision.RunningMode.VIDEO,
                                           score_threshold=0.5)
    detector = vision.ObjectDetector.create_from_options(options)

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Starting MediaPipe Detection. Press 'q' to quit.")
    
    start_time = time.time()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the image from BGR to RGB as required by the TFLite model.
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_image)

        # Calculate timestamp (in milliseconds)
        # MediaPipe requires strictly increasing timestamps
        frame_timestamp_ms = int((time.time() - start_time) * 1000)

        # Run object detection using the model.
        detection_result = detector.detect_for_video(mp_image, frame_timestamp_ms)

        # Visualize the detection results on the frame.
        annotated_image = visualize(frame.copy(), detection_result)

        # Calculate and display FPS
        curr_time = time.time()
        fps = 1.0 / (curr_time - (frame_timestamp_ms/1000.0 + start_time)) # approximate instant FPS
        # Better FPS calc
        # Actually proper variable tracking is safer:
        # We can just use a simple delta
        pass
        # simpler FPS logic for display
    
    # Let's restart the simplified loop with robust FPS
    pass

# Redefining main for clean logic
def run_app():
    # Download check? - We assume model is present (handled by setup steps)
    
    base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
    options = vision.ObjectDetectorOptions(base_options=base_options,
                                           running_mode=vision.RunningMode.VIDEO,
                                           score_threshold=0.5)
    detector = vision.ObjectDetector.create_from_options(options)

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    prev_time = time.time()
    start_program = time.time()

    print("Running MediaPipe... Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret: break

        # MediaPipe needs RGB
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_image)
        
        # Timestamp
        ms = int((time.time() - start_program) * 1000)
        
        # Detect
        result = detector.detect_for_video(mp_image, ms)
        
        # Draw
        annotated_frame = visualize(frame.copy(), result)
        
        # FPS
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time) if curr_time > prev_time else 0
        prev_time = curr_time
        
        cv2.putText(annotated_frame, f"FPS: {int(fps)}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        cv2.imshow('MediaPipe Object Detection', annotated_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_app()
