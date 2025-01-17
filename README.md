# Yolov11-Segmatation
an ai training thing called ultralytics

# IMPORTENT
                          
Download This to use this ai ⬇


[![](https://kajabi-storefronts-production.kajabi-cdn.com/kajabi-storefronts-production/file-uploads/blogs/22606/images/61ae8d7-6831-7f5c-8b52-01d30ba74ffc_og-ultralytics.jpeg)](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11m-seg.pt)


Make sure to have tons of images and rename some to val to make a step easier
also download anaconda

First go to the Directory you are making this in with anaconda prompt

Then Copy this code and put it in

```
conda create -n yolov11_seg python=3.11 -y
```
 

Make sure to download python on mac

then put this in

```
conda activate yolov11_seg
```


then install ultralytics

```
pip install ultralytics
```

also install label-studio
```
pip install label-studio
```

then put the images in the directory your using

then run

```
label-studio
```

then label your pictures

then export ass yolo format and then Download the pt file and then the files up there

create 2 folders called val and train

then put in there location like


ex/ex/ex/yourdirectory/train

for the yaml file
