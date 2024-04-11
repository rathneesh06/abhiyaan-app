import cv2
import numpy as np
import time

# Load the video
cap = cv2.VideoCapture('task4_1.mov')

# Define the lower and upper bounds of the blue color in HSV format
lower_blue = np.array([100, 50, 50])  # Adjust these values as needed
upper_blue = np.array([130, 255, 255])  # Adjust these values as needed

# Variables for velocity and acceleration calculation
prev_center = None
prev_time = None
prev_velocity = None
path_points = []  # List to store center coordinates for drawing the path

while cap.isOpened():
    """ret and frame are diff values , ret says if a particular frame is read 
                                             successfully,frame is numpy array representing an image. """
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame from BGR to HSV color space        #each frame(pic) is converted bgr to hsv as opencv uses hsv format
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask using the specified blue color range       #this creates like a upper and lower threshold to the images (can be tweeked)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Apply morphological operations to remove noise
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Find contours in the mask                                contours  are nothing but the boundaries for the detected object,RETR_EXT only considers external contours
    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)#CHAIN_APPROX_SIMPLE ,This parameter specifies the contour approximation method.


    # Draw the contours on the original frame and calculate velocity and acceleration
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:  # Adjust the area threshold as needed
            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)

            # Calculate the center of the contour
            M = cv2.moments(contour)
            if M["m00"] != 0:
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                path_points.append(center)  # Add center to path points list

                # Calculate velocity if previous center exists
                if prev_center is not None and prev_time is not None:
                    distance = np.sqrt((center[0] - prev_center[0]) ** 2 + (center[1] - prev_center[1]) ** 2)
                    time_diff = time.time() - prev_time
                    velocity = distance / time_diff
                    print("Velocity:", velocity, "pixels/second")

                    # Calculate acceleration if previous velocity exists
                    if prev_velocity is not None:
                        velocity_diff = velocity - prev_velocity
                        acceleration = velocity_diff / time_diff
                        print("Acceleration:", acceleration, "pixels/second^2")

                    # Update previous velocity
                    prev_velocity = velocity

                # Update previous center and time
                prev_center = center
                prev_time = time.time()

    # Draw the path taken by the center of the ball
    for i in range(1, len(path_points)):
        cv2.line(frame, path_points[i - 1], path_points[i], (255, 0, 0), 2)  # Draw a line between consecutive points

    # Display the frame with contours and path
    cv2.imshow('Detected Blue Ball', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
