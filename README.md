# RMBG1.4-python-code
RMBG v1.4 is the latest state-of-the-art model for photo background removal, known for its precision and accuracy. Easily remove backgrounds from images with the following code snippet, which provides consistent, professional results suitable for various applications.


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

