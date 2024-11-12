# !wget https://github.com/camenduru/BRIA-RMBG-1.4-hf/raw/main/briarmbg.py -O briarmbg.py
# !wget https://github.com/camenduru/BRIA-RMBG-1.4-hf/raw/main/input.jpg -O input.jpg
# Reference: https://colab.research.google.com/github/camenduru/bria-rmbg-jupyter/blob/main/bria_rmbg_jupyter.ipynb

import numpy as np
import torch
import torch.nn.functional as F
from torchvision.transforms.functional import normalize
from huggingface_hub import hf_hub_download
from briarmbg import BriaRMBG
import PIL
from PIL import Image
from typing import Tuple
import time 


net=BriaRMBG()
model_path = hf_hub_download("briaai/RMBG-1.4", 'model.pth')

if torch.cuda.is_available():
    net.load_state_dict(torch.load(model_path))
    net=net.cuda()
else:
    net.load_state_dict(torch.load(model_path,map_location="cpu"))
net.eval() 
    
def resize_image(image):
    image = image.convert('RGB')
    model_input_size = (1024, 1024)
    image = image.resize(model_input_size, Image.BILINEAR)
    return image

def remove_bg(image_path):
    orig_image = Image.open(image_path)
    w,h = orig_im_size = orig_image.size
    image = resize_image(orig_image)
    im_np = np.array(image)
    im_tensor = torch.tensor(im_np, dtype=torch.float32).permute(2,0,1)
    im_tensor = torch.unsqueeze(im_tensor,0)
    im_tensor = torch.divide(im_tensor,255.0)
    im_tensor = normalize(im_tensor,[0.5,0.5,0.5],[1.0,1.0,1.0])
    if torch.cuda.is_available():
        im_tensor=im_tensor.cuda()

    result=net(im_tensor)
    result = torch.squeeze(F.interpolate(result[0][0], size=(h,w), mode='bilinear') ,0)
    ma = torch.max(result)
    mi = torch.min(result)
    result = (result-mi)/(ma-mi)    
    im_array = (result*255).cpu().data.numpy().astype(np.uint8)
    pil_im = Image.fromarray(np.squeeze(im_array))
    new_im = Image.new("RGBA", pil_im.size, (0,0,0,0))
    new_im.paste(orig_image, mask=pil_im)
    return new_im



t1 = time.time()
output = remove_bg('image.jpg')
output.save('output_img2.png')
print('Time takes to remove background (seconds): ', time.time() - t1)

