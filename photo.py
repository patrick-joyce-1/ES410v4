import cv2  # import the opencv libraryr
def gstreamer_pipeline(
    capture_width=1080,
    capture_height=720,
    display_width=1080,
    display_height=720,
    framerate=60,
    flip_method=0,
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

filename = 'photo.jpg'

# define a video capture object
vid = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)

# Capture the video frame by frame
ret, frame = vid.read()

cv2.imwrite(filename, frame)  # Using cv2.imwrite() method to the image

vid.release()  # After the loop release the cap object
