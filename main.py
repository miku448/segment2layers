from PIL import Image
from tqdm import tqdm

def extract_layers_from_segmentation(original_path, segmented_path):
    original = Image.open(original_path).convert("RGBA")
    segmented = Image.open(segmented_path).convert("RGB")

    colors = set(segmented.getdata())
    layers = []

    for color in tqdm(colors, desc="Extracting layers", unit="layer"):
        layer = Image.new('RGBA', original.size)

        for x in range(original.width):
            for y in range(original.height):
                if segmented.getpixel((x, y)) == color:
                    layer.putpixel((x, y), original.getpixel((x, y)))
                else:
                    layer.putpixel((x, y), (0, 0, 0, 0))  # Transparent

        layers.append(layer)

    return layers

def merge_layers_into_tiff(layers, tiff_path):
    print("Combining into TIFF...")
    # Save as a multi-layered TIFF
    layers[0].save(tiff_path, save_all=True, append_images=layers[1:])

if __name__ == "__main__":
    layers = extract_layers_from_segmentation("original.png", "segmented.png")
    merge_layers_into_tiff(layers, "output.tif")
