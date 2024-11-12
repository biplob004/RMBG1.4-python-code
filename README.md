# RMBG v1.4 - High-Accuracy Background Removal Model

**RMBG v1.4** is a state-of-the-art background removal model developed by **BRIA AI**. Designed to precisely separate foreground from background across a variety of image types and categories, RMBG v1.4 has been rigorously trained on over 12,000 high-quality, manually labeled images, making it exceptionally effective for applications in **e-commerce**, **gaming**, **advertising**, and more.

### Key Features
- **High Accuracy**: Utilizes a saliency segmentation architecture, achieving superior accuracy compared to other available models.
- **Versatile Applications**: Suitable for diverse use cases, including content creation at scale, with a focus on content safety and bias mitigation.
- **Easy Integration**: Includes Python code for seamless integration, allowing developers to implement background removal in their projects effortlessly.


## Image Comparison: Input vs. Output (Background Removed)

<table>
  <tr>
    <td><strong>Input Image</strong></td>
    <td><strong>Output Image</strong></td>
  </tr>
  <tr>
    <td><img src="img/input_image.jpg" alt="Input Image" width="400"/></td>
    <td><img src="img/output_image.jpg" alt="Output Image" width="400"/></td>
  </tr>
</table>

---

### How to Use

To utilize this code for background removal, follow these steps:

1. **Install Required Packages**  
   Ensure you have all the necessary Python packages by installing them from `requirements.txt`. Run the following command in your terminal:

   ```bash
   pip install -r requirements.txt
   ```

2. **Edit Image Paths**  
   Before executing the main script, open `main.py` and specify the paths for the input and output images:
   - **Input Image Path:** Set the path to the image you want to process.
   - **Output Image Path:** Specify where the processed image (with background removed) should be saved.

3. **Run the Script**  
   After configuring the paths, execute the following command to remove the background from the input image:

   ```bash
   python main.py
   ```

The output image, with the background removed, will be saved at the location you specified.

---

### License Information
RMBG v1.4 is available under a **non-commercial license**. You can use it for **personal projects** and **educational purposes**. For any **commercial use**, please obtain a separate agreement with **BRIA AI**. Ensure compliance with licensing requirements when utilizing or modifying the code in this repository.



**Explore the power of RMBG v1.4 in your applications today!**

