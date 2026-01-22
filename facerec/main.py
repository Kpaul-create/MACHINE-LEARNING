import cv2
import time
from ultralytics import YOLO

def main():
    # Load the YOLOv8 model - using 'n' (nano) for speed
    print("Loading YOLOv8 model...")
    model = YOLO('yolov8n.pt')

    # Initialize webcam
    cap = cv2.VideoCapture(0)
    
    # Set resolution to 640x480 for better performance
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Starting object detection. Press 'q' to quit.")

    # Optimization variables
    frame_count = 0
    skip_frames = 2  # Process 1 out of every (skip_frames + 1) frames. 2 means process every 3rd frame.
    annotated_frame = None
    
    prev_time = 0
    curr_time = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image.")
            break

        frame_count += 1
        
        # Calculate FPS
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time) if prev_time != 0 else 0
        prev_time = curr_time

        # Only run detection every N frames
        if frame_count % (skip_frames + 1) == 0 or annotated_frame is None:
            # Run tracking instead of just detection for better stability
            # conf=0.5 improves accuracy by filtering low-confidence detections
            # persist=True is needed for tracking
            results = model.track(frame, persist=True, conf=0.5, verbose=False)
            
            # Plot results
            annotated_frame = results[0].plot()
        
        # If we skipped a frame, we might want to just display the last annotated frame
        # OR better: draw the last specific boxes on the CURRENT frame. 
        # But for simple visualization, displaying the last processed frame (annotated_frame) 
        # updates the video feed 'stutteringly' if we just hold the image.
        # A better approach for smooth video + fast detection is:
        # detection happens on 1 frame, display happens on ALL frames.
        # But 'annotated_frame' has the boxes drawn ON the image. 
        # If we want smooth video, we should just redraw the overlay on the current frame.
        # However, `plot()` returns a new image. 
        # For simplicity and strictly "better FPS" on the detection loop, we can just show the annotated frame whenever it updates,
        # but that looks laggy. 
        # Instead, let's use the 'annotated_frame' as the thing we show, accepting it might look lower FPS than the camera stream.
        # Actually, let's try to just run detection less often but show every frame?
        # If we run detection less often, we don't have new boxes for the intermediate frames.
        # We can use the LAST known boxes.
        
        # Let's stick to the simple frame skipping for logic:
        # If we skip inference, we just show the raw frame? No, we want to see boxes.
        # Ideally we use an async thread for detection. 
        # But to keep it simple and single-threaded:
        # We will just run tracking EVERY frame but verify if 'skip_frames' helps. 
        # Actually, YOLOv8 'track' is quite fast. 
        # Let's try running track every frame first? The user said FPS is low.
        # Okay, let's stick to the plan: skip frames for INFERENCE.
        # But 'track' needs typically continuous frames. 
        # If we skip frames, tracking might break.
        # Let's reduce resolution and use 'track' on every frame first, 
        # but if that's slow, we use standard detection with skipping.
        # Let's try skipping with standard detection (not track) because tracking needs continuity.
        # OR: We use 'track' but only every 2nd frame? No, track needs the sequence.
        
        # Revised Strategy for 'Optimized':
        # 1. Resize to 640x480 (done).
        # 2. Use 'track' every frame (model is nano, should be fast at 640x480).
        # 3. IF that is too slow, we can't easily skip frames with 'track'.
        # Let's ASSUME the user's "low FPS" was due to high-res webcam default (often 1080p).
        # I will keep track running every frame but ensure the resolution is constrained.
        # Also I'll make sure verbose=False to save console print time.
        
        # Wait, I promised frame skipping in the plan. 
        # If I use frame skipping, I should probably fall back to standard 'predict' 
        # and just draw the LAST known boxes on the current frame during skipped frames.
        
        if frame_count % (skip_frames + 1) == 0:
            results = model(frame, verbose=False, conf=0.5)
            annotated_frame = results[0].plot()
        else:
            # For skipped frames, if we want to show smooth video, we display 'frame' 
            # combined with the *last known* detections. 
            # But results[0].plot() returns a hard-baked image.
            # We would need the boxes to draw them ourselves on the new 'frame'.
            # That's more complex code.
            # A simpler "optimization" that is often acceptable:
            # Just show the annotated frame from the last inference. 
            # It makes the video look like 10fps, but the computer isn't dying.
            
            # However, the user wants "Optimised". 
            # Let's go with: Run 'track' on every frame but at 640x480 on 'n' model.
            # This is usually real-time on most CPUs.
            pass

    # Let's rewrite the loop to be the robust "Track Every Frame" approach first.
    # If I skip inference frames, I can't track well.
    # The biggest killer of FPS is usually printing to stdout or high resolution.
    
    # RE-REVISED STRATEGY based on "low FPS":
    # 1. Force 640x360 or 640x480.
    # 2. Use 'yolov8n.pt' (Nano).
    # 3. Use 'track' with persist=True.
    
    # Let's do this clean version:
    
    pass

def run_optimized():
    print("Loading YOLOv8-Nano model...")
    model = YOLO('yolov8n.pt')

    cap = cv2.VideoCapture(0)
    # Lower resolution for speed
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    prev_frame_time = 0
    new_frame_time = 0

    print("Starting optimized detection...")

    while True:
        ret, frame = cap.read()
        if not ret: 
            break

        # Resize just in case the camera didn't accept the set() command
        # (Some cameras force high res)
        frame = cv2.resize(frame, (640, 480))

        # Run tracking. 
        # conf=0.5 triggers fewer detections (less post-processing drawing) -> slight speedup
        # verbose=False stops printing per-frame stats to terminal -> HUGE speedup on some systems
        results = model.track(frame, persist=True, conf=0.5, verbose=False)

        # Visualize
        annotated_frame = results[0].plot()

        # FPS Calculation
        new_frame_time = time.time()
        fps = 1 / (new_frame_time - prev_frame_time) if prev_frame_time > 0 else 0
        prev_frame_time = new_frame_time
        
        # display FPS on screen
        cv2.putText(annotated_frame, f"FPS: {int(fps)}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Optimized YOLOv8", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_optimized()
