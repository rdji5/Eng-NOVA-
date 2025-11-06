
import cv2
import numpy as np

def normalize_color(frame):
    """Gray world color normalization to reduce lighting effect"""
    result = frame.astype(np.float32)
    avg_b = np.mean(result[:, :, 0])
    avg_g = np.mean(result[:, :, 1])
    avg_r = np.mean(result[:, :, 2])
    avg_gray = (avg_b + avg_g + avg_r) / 3

    result[:, :, 0] = np.minimum(result[:, :, 0] * (avg_gray / avg_b), 255)
    result[:, :, 1] = np.minimum(result[:, :, 1] * (avg_gray / avg_g), 255)
    result[:, :, 2] = np.minimum(result[:, :, 2] * (avg_gray / avg_r), 255)

    return result.astype(np.uint8)

# Initialize camera (USB or Pi camera)
camera = cv2.VideoCapture(0)
camera.set(3, 640)
camera.set(4, 480)

while True:
    ret, frame = camera.read()
    if not ret:
        break

    # Optional: normalize to reduce color cast from lighting
    frame = normalize_color(frame)

    # Convert BGR to LAB
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    L, A, B = cv2.split(lab)

    # --- Detect RED (A-channel is high for red) ---
    red_mask = cv2.inRange(A, 150, 255)   # high A → red
    green_mask = cv2.inRange(A, 0, 110)   # low A → green

    # Clean up noise
    kernel = np.ones((5, 5), np.uint8)
    red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel)
    green_mask = cv2.morphologyEx(green_mask, cv2.MORPH_OPEN, kernel)

    # Find contours for red
    contours_red, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours_red:
        area = cv2.contourArea(c)
        if area > 400:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, "RED", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    # Find contours for green
    contours_green, _ = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours_green:
        area = cv2.contourArea(c)
        if area > 400:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "GREEN", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Display the output
    cv2.imshow("Color Detection (LAB-based)", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key to exit
        break

camera.release()
cv2.destroyAllWindows()
