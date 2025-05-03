import argparse
from utils import generate_from_text, generate_from_image

def main():
    parser = argparse.ArgumentParser(description="Generate 3D models from text or image.")
    parser.add_argument('--text', type=str, help='Text prompt to generate 3D model')
    parser.add_argument('--image', type=str, help='Path to image for 3D model generation')
    args = parser.parse_args()

    if args.text:
        generate_from_text(args.text)
    elif args.image:
        generate_from_image(args.image)
    else:
        print("Please provide either --text or --image argument")

if __name__ == "__main__":
    main()
