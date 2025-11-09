# Pedestrian Zone Vehicle Entry Detection

## Overview
This project aims to detect vehicles that enter restricted pedestrian-only areas using object detection on images. Detecting such illegal entries can help city authorities monitor pedestrian safety and enforce regulations automatically. It belongs to the Automotive theme under AI/ML-based Object Detection.

## Week 1 (Setup & Planning)
- Chosen topic: **Pedestrian Zone Vehicle Entry Detection**
- Collected sample street and pedestrian-area images from Roboflow dataset.
- Created project folder structure (`data/raw`, `data/labels`, `scripts`, `notebooks`, `outputs`).
- Planned annotation and model training in Week 2 using YOLOv5 and LabelImg.
- Added Week-1 report and requirements file to GitHub repository.

## Tools (Planned)
- **Programming:** Python  
- **Libraries:** OpenCV, PyTorch, YOLOv5, NumPy, Matplotlib, Pandas  
- **Annotation Tool:** LabelImg  
- **Environment:** Google Colab  
- **Version Control:** GitHub  

## Next Steps (Week 2)
- Annotate collected images to label vehicles entering pedestrian zones.
- Prepare dataset YAML file for YOLOv5.
- Train YOLOv5 model on Colab using the annotated dataset.
- Save trained weights and run sample detection tests.
- Document model accuracy and inference results.

## Expected Output
A trained AI model that can detect vehicles entering restricted pedestrian-only zones from static images or CCTV frames. The output will display bounding boxes around detected vehicles and a confidence score.

### Week-2 Progress
- Integrated YOLOv5 training script (see `scripts/train_yolov5.py`)
- Dataset from Roboflow (YOLOv5 format) stored under `data/raw`
- Added sample training and detection results in `outputs/`
- Model aims to detect vehicles entering pedestrian zones

## Dataset Source
Dataset partially sourced from Roboflow Universe:
[Vehicle Detection Dataset on Roboflow](https://universe.roboflow.com/final-project-7gql2/vehicle-detection-i66s2)

