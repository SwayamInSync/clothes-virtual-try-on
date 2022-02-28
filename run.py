import os

os.chdir('/content/clothes-virtual-try-on')
os.system("!rm -rf /content/inputs/test/cloth/.ipynb_checkpoints")
os.system("!python cloth-mask.py")
os.system("!python3 /content/Self-Correction-Human-Parsing/simple_extractor.py --dataset 'lip' --model-restore '/content/Self-Correction-Human-Parsing/checkpoints/final.pth' --input-dir '/content/inputs/test/image' --output-dir '/content/inputs/test/image-parse'")
os.chdir('/content')
os.system("!cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/inputs/test/image/ --write_json /content/inputs/test/openpose-json/ --display 0 --render_pose 0 --face --hand")
os.system("!cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/inputs/test/image/ --display 0 --write_images /content/inputs/test/openpose-img/ --hand --render_pose 1 --disable_blending true")

model_image = os.listdir('/content/inputs/test/image')
cloth_image = os.listdir('/content/inputs/test/cloth')
pairs = zip(model_image, cloth_image)

with open('/content/inputs/test_pairs.txt', 'w') as file:
  for model, cloth in pairs:
    file.write(f"{model} {cloth}")

os.system("!python /content/drive/MyDrive/VITON-HD/test.py --name output --dataset_dir /content/inputs --checkpoint_dir /content/drive/MyDrive/VITON-HD/checkpoints --save_dir /content/")
