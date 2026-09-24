from PIL import Image, ImageOps
import sys

def to_bw(input_path, output_path, T=128):
    img = Image.open(input_path)
    img = ImageOps.exif_transpose(img)  # fix phone rotation
    img = img.convert("L")
    bw = img.point(lambda p: 255 if p >= T else 0)
    bw.save(output_path)
    print(f"Saved {output_path}")

if __name__ == "__main__":
    T = int(sys.argv[1]) if len(sys.argv) > 1 else 128
    to_bw("photo.jpg", "output.png", T)
