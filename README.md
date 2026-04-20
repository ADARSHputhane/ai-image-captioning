# AI Image Captioning with BLIP & Flask

A lightweight, responsive web application that uses Hugging Face's BLIP (Bootstrapping Language-Image Pre-training) model to automatically generate descriptive captions for uploaded images. 

This project demonstrates the integration of state-of-the-art machine learning models with a Python backend and an asynchronous JavaScript frontend. To prioritize reliability and bypass network restrictions, the application is configured to run the model entirely locally.

## ✨ Features

* **Local AI Inference:** Runs the Salesforce BLIP model directly from your local storage, eliminating API costs and network-related crashes during inference.
* **Asynchronous Processing:** Utilizes the JavaScript `fetch` API for smooth, reload-free image uploads and loading states.
* **Secure File Handling:** Implements Werkzeug's `secure_filename` to sanitize user uploads and prevent directory traversal attacks.
* **Environment Isolation:** Designed to run within a dedicated Conda environment to strictly manage PyTorch and Transformer dependencies without polluting the global system.

## 🛠️ Tech Stack

* **Backend:** Python 3.10, Flask, Werkzeug
* **Machine Learning:** Hugging Face `transformers`, PyTorch, Torchvision, Pillow (PIL)
* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Version Control:** Git, GitHub, Git LFS

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your machine:
* [Anaconda](https://www.anaconda.com/products/distribution) or Miniconda
* [Git](https://git-scm.com/)
* [Git Large File Storage (LFS)](https://git-lfs.com/) (Required for downloading the model weights)

## 🚀 Installation and Setup

Follow these steps to get the project running on your local machine.

### 1. Clone the Repository
Open your terminal or Anaconda Prompt and clone this repository:
```bash
git clone [https://github.com/YOUR_USERNAME/ai-image-captioning.git](https://github.com/ADARSHputhane/ai-image-captioning.git)
cd ai-image-captioning
```

### 2. Set Up the Conda Environment
```bash
conda create --name blip_env python=3.10 -y
conda activate blip_env
```

### 3. Install requirements.txt file:
```bash
pip install -r requirements.txt
```

### 4.Download the Local Model 
```bash
git lfs install
git clone [https://huggingface.co/Salesforce/blip-image-captioning-base](https://huggingface.co/Salesforce/blip-image-captioning-base)
```

### 5. Run the Application 
```bash
python app.py
```
