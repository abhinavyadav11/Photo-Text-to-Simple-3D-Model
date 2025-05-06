# 🧠 Photo/Text to Simple 3D Model

This project converts either a text prompt (e.g., "a red toy car") or a photo into a simple 3D object (.obj, .ply format) using AI. It uses Salesforce BLIP for image captioning and Shap-E from OpenAI for 3D generation.

<img width="1256" alt="Screenshot 2025-05-06 at 5 12 26 PM" src="https://github.com/user-attachments/assets/5563a679-23ee-4a26-9a08-0fc70f1f24b1" />

## 🔧 Features

✅ Generate 3D model from text prompts  
✅ Generate 3D model from photos (via automatic captioning)  
✅ Supports background removal from image before processing  
✅ Outputs in .obj and .ply formats  

## 📦 Installation

```bash
git clone https://github.com/abhinavyadav11/Photo-Text-to-Simple-3D-Model
cd Photo-Text-to-Simple-3D-Model

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

#Install shap-e
pip install git+https://github.com/openai/shap-e.git
```

## 🚀 Usage
▶ Generate from Text
```bash
python main.py --text "a red toy car"
```

## 🖼️ Generate from Image
```bash
python main.py --image path/to/your/image.jpg
```

## 🗂 Output
Saved to the outputs/ folder:

- generated_model_0.obj
- generated_model_0.ply
- cleaned_image.png (background removed image)

## 📁 Folder Structure

Photo-Text-to-Simple-3D-Model/
├── main.py
├── utils.py
├── requirements.txt
├── outputs/
└── README.md


## 👨‍💻 Author
Abhinav Yadav
