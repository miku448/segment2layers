# segment2layers

A script to extract distinct color-based layers from a segmented image and combine them into a multi-layered TIFF file.

## Installation

1. Clone this repository:
```
git clone https://github.com/miku448/segment2layers.git
cd segment2layers
```

2. Create a virtual environment (optional, but recommended):
```
python3 -m venv venv
source venv/bin/activate
```
3. Install the necessary packages:
```
pip install -r requirements.txt
```

## Usage

First, prepare the segmented image. You can use automatic1111's extension [inpaint anything](https://github.com/Uminosachi/inpaint-anything)
![](/_preview/segment.png)


Run the script by providing the paths to the original image and the segmented image:
```
python main.py
```
Ensure `original.png` and `segmented.png` are present in the script's directory or modify the script to point to their respective paths.

After execution, the layers will be combined into a multi-layered TIFF file named `output.tif`.
![](/_preview/gimp.png)
