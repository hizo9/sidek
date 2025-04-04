# Imports
from ultralytics import YOLO

# Configs
model = YOLO("best_ncnn_model", task="detect")
source = "images"

# Codes
results = model(source, stream=True)

for result in results:
    boxes = result.boxes
    classes = result.names

    result.show()