from importlib import import_module

YOLOv10 = import_module("models.yolo_v10.ultralytics").YOLOv10
inference = import_module("models.yolo_v10.detector").inference
