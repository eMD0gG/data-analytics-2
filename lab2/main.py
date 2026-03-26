import os
import config
import csv

from llm_api import call_llm

def select_input_csv(folder_path="input_data"):
    files = os.listdir(folder_path)
    print(files)
    csv_files = [file for file in files if file.endswith(".csv")]

    if not csv_files:
        print("No csv files found in folder")
        return

    print("Here available files:")
    for i, file in enumerate(csv_files):
        print(f"{i+1}. {file[:-4]}")

    while True:
        try:
            choice = input(f"Enter file number (1-{len(csv_files)}) or 0 for exit: ")
            if choice == "0":
                return None

            index = int(choice) - 1
            if 0 <= index < len(csv_files):
                return os.path.join(folder_path, csv_files[index])
            else:
                print(f"Please enter a valid value")
        except ValueError:
            print("Please enter a valid value")


def read_csv(file_path):
    with open(file_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data

def process_comments(data):
    results = []
    total = len(data)

    for idx, row in enumerate(data, 1):
        print(f"Processing {idx}/{total}...")

        video_title = row["video_title"]
        comment = row["processed_comment"]

        llm_result = call_llm(video_title, comment)

        results.append({
            "comment_id": row["comment_id"],
            "video_title": video_title,
            "comment": comment,
            "sentiment": llm_result["sentiment"],
            "emotion": llm_result["emotion"],
            "intensity": llm_result["intensity"],
            "aspects": ",".join(llm_result["aspects"]),
            "recommendation": llm_result["recommendation"]
        })

    return results


def save_results(results, input_file_path):
    output_folder = config.OUTPUT_FOLDER
    os.makedirs(output_folder, exist_ok=True)

    base_name = os.path.splitext(os.path.basename(input_file_path))[0]
    output_file = os.path.join(output_folder, f"{base_name}_output.csv")

    fieldnames = ["comment_id", "video_title", "comment", "sentiment", "emotion", "intensity", "aspects",
                  "recommendation"]

    file_exists = os.path.isfile(output_file)

    with open(output_file, 'a', newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerows(results)

    print(f"Results saved to {output_file}")


def pipeline():
    file_path = select_input_csv()
    if not file_path:
        print("No file selected")
        return

    data = read_csv(file_path)
    results = process_comments(data)
    save_results(results, file_path)

if __name__ == "__main__":
    pipeline()