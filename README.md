# 🧠 Photo/Text to Simple 3D Model

This project converts either a **text prompt** (e.g., "a red toy car") or a **photo** into a simple 3D object (`.obj`, `.ply` format) using AI. It uses [Salesforce BLIP](https://github.com/salesforce/BLIP) for image captioning and [Shap-E](https://github.com/openai/shap-e) from OpenAI for 3D generation.

---

## 🔧 Features

- ✅ Generate 3D model from **text prompts**
- ✅ Generate 3D model from **photos** (via automatic captioning)
- ✅ Supports background removal from image before processing
- ✅ Outputs in `.obj` and `.ply` formats

---

## 📦 Installation

```bash
git clone https://github.com/abhinavyadav11/Photo-Text-to-Simple-3D-Model
cd Photo-Text-to-Simple-3D-Model

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
