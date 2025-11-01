# Week-1 Report — Pedestrian Zone Vehicle Entry Detection

**1. Project Title:**  
Pedestrian Zone Vehicle Entry Detection using Object Detection

**2. Objective:**  
To automatically detect and highlight vehicles that enter pedestrian-only zones in static images, helping city authorities ensure pedestrian safety and monitor rule violations.

**3. Problem Statement:**  
Pedestrian zones are intended for safe walking, yet vehicles sometimes enter these areas illegally, endangering people and disrupting flow. Manual monitoring is costly and inconsistent. Using AI-based image analysis, we can detect vehicles entering such zones automatically and alert authorities in real time.

**4. Tools & Technologies (Planned):**  
- Python  
- OpenCV  
- PyTorch  
- YOLOv5 (Ultralytics)  
- LabelImg  
- Google Colab  
- GitHub  

**5. Dataset (Week 1 Status):**  
- **Source:** Roboflow Vehicle Detection Dataset  
  [https://universe.roboflow.com/final-project-7gql2/vehicle-detection-i66s2](https://universe.roboflow.com/final-project-7gql2/vehicle-detection-i66s2)  
- **Images Collected:** 20–30 street-scene and pedestrian-zone images  
- **Stored In:** `data/raw/` folder  
- **Labels:** Not yet annotated — `data/labels/` folder created for Week 2 labeling.

**6. Work Done This Week:**  
- Selected the project topic under the Automotive Object Detection theme.  
- Researched similar vehicle detection use-cases.  
- Created GitHub repository and structured folders (`data/raw`, `data/labels`, `notebooks`, `scripts`, `outputs`).  
- Collected sample images and uploaded them to the repository.  
- Added required files: `README.md`, `requirements.txt`, `.gitignore`, and this report.  
- Planned the labeling and training workflow for Week 2.

**7. Expected Output:**  
A detection model that identifies vehicles entering pedestrian-only zones and marks them with bounding boxes in images or video frames, providing visual evidence and confidence scores.

**8. Week-2 Plan (Brief):**  
- Annotate all images using **LabelImg** (YOLO format).  
- Split data into training and validation sets.  
- Train a baseline YOLOv5 model on Google Colab.  
- Save trained weights and visualize detections.  
- Document accuracy metrics (precision, recall, mAP).

**9. GitHub Repository:**  
https://github.com/1nt22ee108vaishnavi-art/pedestrian-zone-vehicle-detection
**Prepared by: Vaishnavi Jatti 
**Duration:** Week 1 of Shell AI/ML Virtual Internship (Automotive Theme)
