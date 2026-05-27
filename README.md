# AI Smart Surveillance System

An AI-powered real-time smart surveillance system built using **YOLOv8**, **DeepSORT**, **FastAPI**, and **OpenCV** for multi-object tracking, people counting, and video analytics.

This system detects and tracks people in real-time using webcam/video input, assigns persistent tracking IDs, performs live people counting, and exposes REST APIs for video processing.

---

#  Features

##  Real-time Object Detection
- Uses YOLOv8 for high-speed person detection
- Detects objects directly from webcam or uploaded video

---

##  Multi-Object Tracking
- Uses DeepSORT for:
  - Persistent object IDs
  - Re-identification across frames
  - Real-time tracking

---

##  People Counting
- Counts total unique people detected
- Displays live people count on video frames

---

##  REST API Backend
Built using FastAPI.

Supports:
- Video upload APIs
- Tracking APIs
- Analytics APIs

---

##  Processed Video Generation
- Saves output tracked video
- Displays:
  - Bounding boxes
  - Tracking IDs
  - People count

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

# 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Object Detection | YOLOv8 |
| Object Tracking | DeepSORT |
| Backend | FastAPI |
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
│
├── test.py
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

Uploads and processes video with:
- YOLOv8 detection
- DeepSORT tracking
- People counting

---

# 📊 Current Capabilities

The system currently supports:

- Real-time webcam tracking
- Persistent tracking IDs
- Multi-person tracking
- People analytics
- REST API backend
- Video upload processing

---

#  Example Output

The processed output video contains:

✅ Bounding boxes  
✅ Tracking IDs  
✅ Live people count  

Example:

```text
People Count: 3
ID: 1
ID: 2
ID: 3
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


