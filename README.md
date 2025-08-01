# 🪖 Helmet Detection Web App

This project is a real-time helmet detection system built using [YOLOv5](https://github.com/ultralytics/yolov5), PyTorch, and Streamlit. It detects whether a person in an image is wearing a helmet or not (`with_helmet` or `without_helmet`).

---

## 🚀 Features

- 🔍 Detects helmets in uploaded images using a custom-trained YOLOv5 model
- 🎨 Streamlit-based web interface for easy interaction
- 🧠 Supports confidence score thresholding
- ✅ Highlights results as "with helmet" or ❌ "without helmet"

---

## 🧰 Tech Stack

- [YOLOv5](https://github.com/ultralytics/yolov5) for object detection
- [PyTorch](https://pytorch.org/) as the deep learning framework
- [Streamlit](https://streamlit.io/) for the web application
- Python 3.12+

---

## 📸 Demo Screenshot

![Helmet Detection Screenshot]
![Screenshot 2025-06-23 155817](https://github.com/user-attachments/assets/cfe619b6-5d75-43fc-bacf-c6c59589beb6)


<!-- Optional: Replace with your own screenshot -->

---

## 📦 Installation

```bash
git clone https://github.com/Asrithkarthikeya/Helmet-Detection-App.git
cd helmet-detection-app
pip install -r requirements.txt
streamlit run app.py (or) python -m streamlit run app.py
