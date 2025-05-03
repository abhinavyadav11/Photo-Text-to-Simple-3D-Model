import torch
from shap_e.diffusion.sample import sample_latents
from shap_e.diffusion.gaussian_diffusion import diffusion_from_config
from shap_e.models.download import load_model, load_config
from shap_e.util.notebooks import create_pan_cameras, decode_latent_mesh, decode_latent_images
from shap_e.util.notebooks import gif_widget
from PIL import Image
import rembg
import os

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
xm = load_model('transmitter', device=device)
model = load_model('text300M', device=device)
diffusion = diffusion_from_config(load_config('diffusion'))

def generate_latents(prompt: str, batch_size=1):
    latents = sample_latents(
        batch_size=batch_size,
        model=model,
        diffusion=diffusion,
        guidance_scale=15.0,
        model_kwargs=dict(texts=[prompt] * batch_size),
        progress=True,
        clip_denoised=True,
        use_fp16=True,
        use_karras=True,
        karras_steps=32,
        sigma_min=1e-3,
        sigma_max=160,
        s_churn=0,
    )
    return latents

def save_3d_model(latents):
    for i, latent in enumerate(latents):
        mesh = decode_latent_mesh(xm, latent).tri_mesh()
        obj_path = f'outputs/example_mesh_{i}.obj'
        ply_path = f'outputs/example_mesh_{i}.ply'
        with open(obj_path, 'w') as f:
            mesh.write_obj(f)
        with open(ply_path, 'wb') as f:
            mesh.write_ply(f)
        print(f"Saved: {obj_path} and {ply_path}")

def generate_from_text(prompt: str):
    print(f"Generating 3D model from text: '{prompt}'")
    latents = generate_latents(prompt)
    save_3d_model(latents)

def remove_background(image_path):
    with open(image_path, "rb") as inp_file:
        input_bytes = inp_file.read()
    output_bytes = rembg.remove(input_bytes)
    output_path = "outputs/cleaned_image.png"
    with open(output_path, "wb") as out_file:
        out_file.write(output_bytes)
    return output_path

def generate_from_image(image_path: str):
    print(f"Processing image: {image_path}")
    clean_image_path = remove_background(image_path)
    print(f"Background removed. Using image to infer prompt...")

    # Very basic prompt guessing from filename (improve this with image captioning if needed)
    guessed_prompt = "a toy car" if "car" in image_path else "a simple object"

    print(f"Guessed prompt: {guessed_prompt}")
    generate_from_text(guessed_prompt)
