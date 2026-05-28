
# SmartVision-Tracker

An AI-powered real-time smart surveillance system built using **YOLOv8**, **DeepSORT**, **FastAPI**, and **OpenCV** for multi-object tracking, people counting, and video analytics.

This system detects and tracks people in real-time using webcam/video input, assigns persistent tracking IDs, performs live people counting, and exposes REST APIs for video processing.

---

#  Features

##  Real-time Object Detection
- Uses YOLOv8 for high-speed person detection
- Detects people directly from webcam or uploaded video
- Real-time inference using PyTorch backend

---

##  Multi-Object Tracking
- Uses DeepSORT for:
  - Persistent tracking IDs
  - Multi-object tracking
  - Re-identification across frames
  - Real-time movement tracking

---

##  People Counting Analytics
- Counts currently visible tracked people
- Prevents repeated counting of same person
- Displays live people count on processed frames

---

##  REST API Backend
Built using FastAPI.

Supports:
- Video upload APIs
- Tracking APIs
- Analytics APIs
- Video processing backend

---

##  Processed Video Generation
The system generates processed surveillance videos containing:
- Bounding boxes
- Tracking IDs
- People count analytics

---

# 🧠 System Architecture

```text
                ┌─────────────────────┐
                │ Webcam / Video Feed │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ YOLOv8 Detection    │
                │ Person Detection    │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ DeepSORT Tracking   │
                │ Unique Tracking IDs │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Analytics Engine    │
                │ People Counting     │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ FastAPI Backend     │
                │ REST APIs           │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Processed Output    │
                │ Video + Analytics   │
                └─────────────────────┘
```

---

# 🎥 Demo Output

##  Real-time Tracking Output

The processed output video contains:
- Person detection
- Persistent tracking IDs
- Live people count
- Multi-object tracking

### Example Output

```text
People Count: 3

ID: 1
ID: 2
ID: 3
```

---

## 📹 Demo Video


Example:

```md
https://github.com/vniharika33/SmartVision-Tracker/blob/main/assets/demo.gif
```


---

# 🌐 FastAPI Swagger Interface

The backend APIs are exposed using FastAPI.

Swagger documentation is automatically generated.

## Swagger Docs

```text
http://127.0.0.1:8000/docs
```

(https://github.com/vniharika33/SmartVision-Tracker/blob/main/assets/swagger.jpeg)



# 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Object Detection | YOLOv8 |
| Object Tracking | DeepSORT |
| Backend Framework | FastAPI |
| Computer Vision | OpenCV |
| Deep Learning | PyTorch |
| API Server | Uvicorn |

---

# 📂 Project Structure

```text
SmartVision-Tracker/
│
├── backend/
│   ├── detector.py
│   ├── tracker.py
│   └── main.py
│
├── videos/
├── outputs/
├── assets/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/vniharika33/SmartVision-Tracker.git
```

---

## 2️⃣ Move Into Project Folder

```bash
cd SmartVision-Tracker
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 4️⃣ Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## 5️⃣ Install Dependencies

```bash
pip install ultralytics
pip install deep-sort-realtime
pip install fastapi
pip install uvicorn
pip install opencv-python
```

---

# ▶️ Run Real-Time Tracking

```bash
python backend/detector.py
```

---

# ▶️ Run FastAPI Backend

```bash
uvicorn backend.main:app --reload
```

---

# 🌐 API Endpoints

##  Home Route

```http
GET /
```

Returns:

```json
{
  "message": "AI Smart Surveillance API Running"
}
```

---

##  Track Video API

```http
POST /track-video
```

Uploads and processes surveillance video using:
- YOLOv8 detection
- DeepSORT tracking
- People analytics

Processed output video is saved automatically.

---

# 📊 Current Capabilities

The system currently supports:

  Real-time webcam tracking  
  Multi-person tracking  
  Persistent tracking IDs  
  People counting analytics  
  REST API backend  
  Video upload processing  
  Processed video generation  

---

#  Example Workflow

```text
Video Input
      ↓
YOLOv8 Detection
      ↓
DeepSORT Tracking
      ↓
People Analytics
      ↓
FastAPI Backend
      ↓
Processed Output Video
```

---

# 🧪 Future Improvements

- Entry/Exit counting
- Heatmap analytics
- Suspicious activity detection
- Vehicle tracking
- Streamlit frontend
- Cloud deployment
- Multi-camera support
- Database integration

---

