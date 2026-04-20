# AI Image Captioning with BLIP & Flask

A lightweight, responsive web application that uses Hugging Face's BLIP (Bootstrapping Language-Image Pre-training) model to automatically generate descriptive captions for uploaded images. 

This project demonstrates the integration of state-of-the-art machine learning models with a Python backend and an asynchronous JavaScript frontend, focusing on clean architecture and local deployment.

## ✨ Features
* **Local AI Inference:** Bypasses network restrictions and API costs by running the Salesforce BLIP model entirely locally.
* **Asynchronous Processing:** Utilizes JavaScript `fetch` API for smooth, reload-free image uploads and loading states.
* **Secure File Handling:** Implements `werkzeug.utils.secure_filename` to sanitize user uploads and prevents arbitrary file execution.
* **Environment Management:** Designed to run within an isolated Conda environment to strictly manage PyTorch and Transformer dependencies.

## 🛠️ Tech Stack
* **Backend:** Python, Flask, Werkzeug
* **AI/ML:** Hugging Face `transformers`, PyTorch, Pillow (PIL)
* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Version Control:** Git, GitHub

## 🚀 Installation and Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/ai-image-captioning.git](https://github.com/YOUR_USERNAME/ai-image-captioning.git)
cd ai-image-captioning
