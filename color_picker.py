import cv2
import numpy as np

# Global variables to store the image and picked color
img = cv2.imread("test_imgs/c1.jpeg")
picked_color = np.array([0, 0, 0]) # Default to black (BGR)
hsv_color = np.array([0,0,0])

# Mouse callback function
def mouse_callback(event, x, y, flags, param):
    global picked_color, hsv_color, img

    if event == cv2.EVENT_LBUTTONDOWN:
        # Get the BGR color of the pixel at (x, y)
        picked_color = img[y, x] # Returns a numpy array 
        hsv_color = cv2.cvtColor(np.uint8([[picked_color]]), cv2.COLOR_BGR2HSV)[0][0]
        print("--------------------")
        print(f"Picked BGR color: {picked_color}")
        print(f"Picked HSV color: {hsv_color}")

cv2.putText(img, "Click to pick color", (100, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

# Create a window and set the mouse callback
cv2.namedWindow("Color Picker")
cv2.setMouseCallback("Color Picker", mouse_callback)

while True:
    # Display the image
    display_img = img.copy()
    
    # Display the picked color in a rectangle
    cv2.rectangle(display_img, (10, 10), (100, 50), picked_color.tolist(), -1)
    cv2.putText(display_img, f"BGR: {picked_color[0]},{picked_color[1]},{picked_color[2]}", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
    cv2.putText(display_img, f"HSV: {hsv_color[0]},{hsv_color[1]},{hsv_color[2]}", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 1)

    cv2.imshow("Color Picker", display_img)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()