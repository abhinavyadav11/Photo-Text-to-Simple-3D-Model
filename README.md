# 🧱 3D Model Generator from Text or Image

This project generates a basic 3D model (`.obj` or `.ply`) from either:
- A text prompt like `"a small toy car"`
- An image with a clear object

It uses OpenAI’s Shap-E model and other open-source libraries.

---

## 🧠 Features

- Accepts text or image input
- Removes background from image (using rembg)
- Generates `.obj` and `.ply` files
- Output can be opened in Blender or any 3D viewer

---

## 🚀 How to Run

1. Clone and install dependencies:

```bash
python -m venv venv
source venv/bin/activate 
pip install -r requirements.txt

# Run with a text prompt:
python main.py --text "a small red toy truck"

# Run with an image input:
python main.py --image examples/input_image.jpg
