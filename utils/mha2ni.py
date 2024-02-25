import os
import SimpleITK as sitk

input_folder = "LOLA11/"
output_folder = "LOLA11_NII/"

def main():
    os.makedirs(output_folder, exist_ok=True)
    input_files = os.listdir(input_folder)

    for input_file in input_files:
        if input_file.endswith(".mha"):
            input_path = os.path.join(input_folder, input_file)
            output_path = os.path.join(output_folder, input_file.replace(".mha", ".nii"))

            img = sitk.ReadImage(input_path)
            sitk.WriteImage(img, output_path)

    print("All exams converted for .nii format.")

if __name__ == "__main__":
    main()
