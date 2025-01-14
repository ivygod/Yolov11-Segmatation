from ultralytics iport YOLO
// You Must download the file in the read me file
model = YOLO("yolo11m-seg.pt")
// add amount of epochs 
model.train(source = "dataset_custom.yaml", batch = 8, workers = 0, device = "cpu", epochs = ?)
