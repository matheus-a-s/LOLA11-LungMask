import os
import nibabel as nib
import numpy as np

pred_folder = "LOLA11_PRED2"
gt_folder = "LOLA11_GT"

index_mapping = {10: 1, 11: 2, 12: 3, 13: 4, 14: 5}
classes = ["lung_upper_lobe_left", "lung_lower_lobe_left", "lung_upper_lobe_right", 
           "lung_middle_lobe_right", "lung_lower_lobe_right"]

def read_nii(file_path):
    img = nib.load(file_path)
    data = img.get_fdata()
    return data

def jaccard_index(gt, pred):
    intersection = np.logical_and(gt, pred)
    union = np.logical_or(gt, pred)
    jaccard = np.sum(intersection) / np.sum(union)
    return jaccard

def save_metrics_to_txt(file_path, metrics):
    with open(file_path, "w") as file:
        for cls, metric in metrics.items():
            file.write(f"Jaccard for {cls}: {metric:.4f}\n")
        file.write("\n")

def main():
    pred_files = os.listdir(pred_folder)

    all_metrics = {cls: [] for cls in classes}

    for input_file in pred_files:
        if input_file.endswith(".nii"):
            pred_path = os.path.join(pred_folder, input_file)
            gt_path = os.path.join(gt_folder, input_file.replace("pred.nii", "GT.nii"))

            print(f"Calculando Jaccard para o exame: {pred_path}")

            pred_data = read_nii(pred_path)
            gt_data = read_nii(gt_path)

            metrics = {}

            for i, (gt_index, pred_index) in enumerate(index_mapping.items()):
                gt_class = (gt_data == gt_index).astype(np.uint8)
                pred_class = (pred_data == pred_index).astype(np.uint8)
                
                jaccard = jaccard_index(gt_class, pred_class)
                metrics[classes[i]] = jaccard
                all_metrics[classes[i]].append(jaccard)

            metrics_file_path = os.path.join(pred_folder, input_file.replace("pred.nii", "metrics.txt"))
            save_metrics_to_txt(metrics_file_path, metrics)

    final_metrics = os.path.join(pred_folder, "final_metrics.txt")
    with open(final_metrics, "w") as file:
        for cls, metrics_list in all_metrics.items():
            mean = np.mean(metrics_list)
            std = np.std(metrics_list)
            minimum = np.min(metrics_list)
            maximum = np.max(metrics_list)
            median = np.median(metrics_list)

            file.write(f"Statistics for class {cls}:\n")
            file.write(f"Mean: {mean:.4f}\n")
            file.write(f"Std: {std:.4f}\n")
            file.write(f"Min: {minimum:.4f}\n")
            file.write(f"Max: {maximum:.4f}\n")
            file.write(f"Median: {median:.4f}\n\n")

if __name__ == "__main__":
    main()