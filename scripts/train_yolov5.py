# train_yolov5.py
# This script trains YOLOv5 on the pedestrian vehicle detection dataset.

# Clone YOLOv5 repo
!git clone https://github.com/ultralytics/yolov5.git
%cd yolov5
!pip install -r requirements.txt

# Unzip dataset (previously downloaded from Roboflow)
!unzip -q "../data/raw/PedestrianVehicleDetection.zip" -d "../data/"

# Train model
!python train.py --img 416 --batch 8 --epochs 20 --data ../data/data.yaml --weights yolov5s.pt --project ../outputs --name vehicle_model

print("Training complete! Check the outputs folder for results.")
