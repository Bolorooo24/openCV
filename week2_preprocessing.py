import cv2
import os

def process_and_save_images(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        image_path = os.path.join(input_dir, filename)

    
        image = cv2.imread(image_path)
        if image is None:
            print(f"reading image error{image_path}. skip.")
            continue

   
        blurred = cv2.GaussianBlur(image, (31, 31), 0) 
        abs_diff = 255 - cv2.absdiff(image, blurred) 


        output_path = os.path.join(output_dir, filename)
        cv2.imwrite(output_path, abs_diff)
        print(f"saved processed image in {output_path}")


input_dir = r"\\192.168.124.213\hawkaeye_l\Itoh-Optical\L-ST00-002\RF\dataset\TrainDataset\v8.1.3\OK"
output_dir = r"\\192.168.124.213\hawkaeye_l\Itoh-Optical\L-ST00-002\RF\dataset\TrainDataset\v8.1.3\abs_diff"
process_and_save_images(input_dir, output_dir)
