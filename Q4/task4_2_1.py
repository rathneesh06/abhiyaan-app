import cv2
import numpy as np
import time

# Load the video
cap = cv2.VideoCapture('videos')

# Define the lower and upper bounds for green color in HSV format
lower_green = np.array([35, 50, 50])
upper_green = np.array([120, 255, 255])

# Create video writers for each ball
video_writers = [cv2.VideoWriter(f'ball_{i+1}.avi', cv2.VideoWriter_fourcc(*'XVID'), 25, (640, 480)) for i in range(5)]

frame_count = 0

# Initialize variables to store previous centroids and paths for each ball
prev_centroids = [None] * 5

frame_rate = cap.get(cv2.CAP_PROP_FPS)

while cap.isOpened():
    """ret and frame are diff values , ret says if a particular frame is read 
                                                 successfully,frame is numpy array representing an image. """
    ret, frame = cap.read()
    if not ret:
        break
    #each frame(pic) is converted bgr to hsv as opencv uses hsv format

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Apply morphological operations to remove noise
    mask = cv2.inRange(hsv, lower_green, upper_green)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
#find contours  contours  are nothing but the boundaries for the detected object,RETR_EXT only considers external contours
    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)#CHAIN_APPROX_SIMPLE ,This parameter specifies the contour approximation method.

    centers = []  # Store the centers of the detected contours

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:
            # Calculate centroid of the contour
            M = cv2.moments(contour)

            """" Zeroth Moment (m00): Represents the total area of the contour. It's the summation of all the pixel values within the contour region.
            cX = int(M["m10"] / M["m00"]): If the area is non-zero (m00 is not zero), this line calculates the x-coordinate of the centroid (cX).
             The first moment m10 represents the sum of the product of pixel intensities and their x-coordinates within the contour.
              Dividing m10 by m00 gives the average x-coordinate, which is the x-coordinate of the centroid."""""

            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                centers.append((cX, cY))

                # Draw contours around the ball
                color=(255,0,0)
                cv2.drawContours(frame, [contour], -1, color, 2)

    # Calculate velocities and accelerations
    for i, center in enumerate(centers):
        if i < len(prev_centroids) and prev_centroids[i] is not None:
            delta_pos = np.array(center) - np.array(prev_centroids[i])

            # Calculate velocity
            time_elapsed=1/frame_rate
            velocity = delta_pos / time_elapsed

            # Calculate acceleration
            if frame_count > 1 and i > 0:
                prev_velocity = np.array(prev_centroids[i]) - np.array(prev_centroids[i - 1])
                acceleration = (velocity - prev_velocity)/time_elapsed
            else:
                acceleration = np.zeros(2)

            # Print velocities and accelerations
            print(f'Frame {frame_count}, Ball {i + 1}:')
            print(f'Velocity: {velocity}')
            print(f'Acceleration: {acceleration}')

    prev_centroids = centers

    # Write the frame to all video writers
    for writer in video_writers:
        writer.write(frame)

    cv2.imshow('Detected green Balls', frame)

    frame_count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and video writers
cap.release()
for writer in video_writers:
    writer.release()

cv2.destroyAllWindows()
