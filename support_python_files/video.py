import cv2
import numpy as np
import matplotlib.pyplot as plt
import torch
from PIL import Image

# from models.experimental import attempt_load
# import torch.backends.cudnn as cudnn
# from utils.datasets import LoadStreams, LoadImages
# from utils.general import check_img_size, non_max_suppression, apply_classifier, scale_coords, xyxy2xywh, \
#     strip_optimizer, set_logging, increment_path
# from utils.plots import plot_one_box
# from utils.torch_utils import select_device, load_classifier, time_synchronized


# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
file = input('input detection file: ')
file_path = '/Users/thomas/Desktop/galvanize/capstone_2/social_distancing_detector/yolov5/runs/detect/'+file
print(file_path)
cap = cv2.VideoCapture(file_path)

# Path to model and best weights
weights_path = '/Users/thomas/Desktop/galvanize/capstone_2/social_distancing_detector/yolov5/runs/train/exp6/weights/best.pt'
model_path = '/Users/thomas/Desktop/galvanize/capstone_2/social_distancing_detector/yolov5/yolov5x.pt'


# # # Model
# # model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True).autoshape()  # for PIL/cv2/np inputs and NMS

# # # Images
# # img1 = Image.open('zidane.jpg')
# # img2 = Image.open('bus.jpg')
# # imgs = [img1, img2]  # batched list of images

# # # Inference
# # prediction = model(imgs, size=640)  # includes NMS



# # Model
#                 # # Load model
#                 # model = attempt_load(weights, map_location=device)  # load FP32 model
#                 # imgsz = check_img_size(imgsz, s=model.stride.max())  # check img_size
# #model = torch.load('best.pt')  # for PIL/cv2/np inputs and NMS
# model = 'runs/train/exp6/weights/best.pt'
# # model = torch.load('tensor.pt')
# # model.eval()
# device = select_device(opt.device)
# model = attempt_load('runs/train/exp6/weights/best.pt', map_location=device)


# Check if camera opened successfully
if (cap.isOpened()== False):
  print("Error opening video stream or file")
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()

  #img = Image.open(frame)

  if ret == True:
    # Inference
    #img_pred = model(frame, size=640)  # includes NMS
    # Display the resulting frame
    cv2.imshow('img_pred', frame)
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
  # Break the loop
  else:
    break
# When everything done, release the video capture object
cap.release()
# Closes all the frames
cv2.destroyAllWindows()

