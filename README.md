# Classroom Attention Monitor

A **vision-based system for non-intrusive attention and sleepiness monitoring** in classroom environments using **Computer Vision, MediaPipe, and Python**.

This project was developed as a **professional portfolio and academic project**, focusing on applied Artificial Intelligence, ethical design, and real-world constraints. The system provides **collective attention insights** to support educators, without performing facial recognition or storing personal identities.

---

## 🎯 Project Motivation

Maintaining student attention in classroom environments is a known challenge. This project explores how **computer vision techniques** can be used to detect **visual indicators associated with sleepiness and reduced attention**, offering aggregated feedback to educators while preserving privacy.

Rather than monitoring individuals, the system focuses on **group-level analysis**, aligning with ethical and privacy-aware AI principles.

---

## 🚀 Features

* Multi-face detection and tracking
* Facial landmarks extraction using MediaPipe
* Eye Aspect Ratio (EAR) analysis
* Detection of visual indicators associated with sleepiness
* Temporary and anonymous face IDs (no identity tracking)
* Collective attention metrics
* Real-time monitoring
* Privacy-preserving and ethical design

---

## 🧠 How It Works

1. Capture video frames from a camera or video source
2. Detect multiple faces using MediaPipe
3. Extract facial landmarks
4. Compute visual indicators (e.g., eye closure duration)
5. Track faces with temporary anonymized IDs
6. Aggregate attention and sleepiness indicators
7. Generate collective insights and alerts

---

## 🏗️ Project Structure

```
classroom-attention-monitor/
│
├── src/            # Core computer vision and analysis logic
├── dashboard/      # Visualization and dashboard 
├── docs/           # Documentation and architecture notes
├── assets/         # Images or diagrams (no personal data)
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🧪 Testing and Validation

Due to the difficulty of accessing real classroom environments, this project is validated using:

* Publicly available classroom and lecture videos
* Recorded simulated classroom scenarios

These tests are used **solely for technical validation**, such as evaluating detection robustness, tracking stability, and performance.

No images or personal data are stored.

---

## ⚠️ Ethical Considerations

This project was designed with ethics and privacy as core principles:

* No facial recognition is performed
* No personal identities are stored or inferred
* Only temporary anonymized IDs are used
* Analysis focuses on collective behavior, not individuals
* The system is not intended for medical or psychological diagnosis

The goal is to provide **supportive insights**, not surveillance.

---

## 🛠️ Technologies

* Python 3.10+
* MediaPipe
* OpenCV
* NumPy
* (Optional) Streamlit for dashboards

---

## 📌 Use Cases

* Academic research and experimentation
* Applied AI portfolio project
* Classroom engagement analysis (experimental)
* Computer vision system design demonstration

---

## 🚧 Roadmap

* [ ] Multi-face detection MVP
* [ ] Face tracking with temporary IDs
* [ ] Eye Aspect Ratio (EAR) implementation
* [ ] Sleepiness indicator logic
* [ ] Collective attention metrics
* [ ] Real-time alerts
* [ ] Dashboard visualization

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👤 Author

Developed by **Pedro Lucas** as a professional and academic project in applied Artificial Intelligence.

---

## ⭐ Acknowledgements

* MediaPipe by Google
* Open-source Computer Vision community

---

*This project is under active development.*
