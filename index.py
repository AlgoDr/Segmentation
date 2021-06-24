# Importing Dependency
import pixellib
from pixellib.instance import instance_segmentation
import cv2

# Loading Model
segmentation_model = instance_segmentation()
segmentation_model.load_model('mask_rcnn_coco.h5')

# Capturing Video Instance On Screen
cap = cv2.VideoCapture(0) # For Webcame Put 0 without '' quotes in function and for running on single video put videopath in '<path-to-video.mp4>' singlequotes in place of zero in videocapturefunction() 
while cap.isOpened():
    ret, frame = cap.read()
    
    # Apply instance segmentation
    res = segmentation_model.segmentFrame(frame, show_bboxes=True)
    image = res[1]
    
    cv2.imshow('Instance Segmentation', image)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
