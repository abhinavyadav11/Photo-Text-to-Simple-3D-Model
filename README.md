🧠 Photo/Text to Simple 3D Model
This project converts either a text prompt (e.g., "a red toy car") or a photo into a simple 3D object (.obj, .ply format) using AI. It uses Salesforce BLIP for image captioning and Shap-E from OpenAI for 3D generation.
🔧 Features

✅ Generate 3D model from text prompts
✅ Generate 3D model from photos (via automatic captioning)
✅ Supports background removal from image before processing
✅ Outputs in .obj and .ply formats

📦 Installation
git clone https://github.com/abhinavyadav11/Photo-Text-to-Simple-3D-Model
cd Photo-Text-to-Simple-3D-Model

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

🚀 Usage
▶ Generate from Text
python main.py --text "a red toy car"

🖼️ Generate from Image
python main.py --image path/to/your/image.jpg

🗂 Output
Saved to the outputs/ folder:

generated_model_0.obj
generated_model_0.ply
cleaned_image.png (background removed image)

💡 System Requirements

⚠️ GPU strongly recommended
On CPU (e.g., MacBook), generation can take 30–60 minutes
On GPU (e.g., Colab Pro or local NVIDIA), time reduces to 2–5 minutes

☁️ Run on Google Colab (Recommended)
You can run this on Colab Pro for faster results. Set up Google Drive to export the .obj files after generation.
📁 Folder Structure
Photo-Text-to-Simple-3D-Model/
├── main.py
├── utils.py
├── requirements.txt
├── outputs/
└── README.md

🧹 Recommended .gitignore
Create a .gitignore file with:
venv/
__pycache__/
*.pyc
outputs/

👨‍💻 Author
Abhinav Yadav
