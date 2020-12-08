# Social_Distancing_Detector
## Motivations


As COVID-19 begins to spike again all over the country, it is more important than ever to continue to social distance from people outside of your household. A tool that can be used by law enforcement agencies, public health care agencies, and others is a social distancing detector. Utilizing YOLOv5, I created a Fully Convolutional neural network (FCNN) that does just that. 


## Datasets

### Image Datasets
* Training Data
  * Consists of 300 images
  * Web Scapped off Google Image Manually
  * Annotated Categories Using Makesense.ai
  * Contaings three categories:
    * man
    * woman
    * child
    
* Validation Data
  * Consists of 50 images
  * Web Scapped off Google Image Manually
  * Annotated Categories Using Makesense.ai
  * Contaings three categories:
    * man
    * woman
    * child
    
* Testing Data
  * Consists of 200 images
  * Web Scapped off Google Image Manually
  
  
### Video Dataset
* 43 minutes of video footage
* Video footage from security camera in parking lot


### Credit to Yolo
Yolov5 is the newest version of YOLO, which is a real-time object detection framework and stands for You Only Look Once. Meaning the image is only passed once through the FCNN or Fully Convolutional neural network.

