from datasets import load_dataset, Dataset
import pandas as pd
from tqdm import tqdm

def process_data(split):
    processed_data = []

    for d in tqdm(split):
        parts = d["text"].split('### Input:')
        instruction = parts[0].strip()

        if len(parts) > 1:
            input_response = parts[1].split('### Response:')
            input_text = input_response[0].strip()
            input_text = "### Input: " + input_text
            response = input_response[1].strip() if len(input_response) > 1 else ""
            response = "### Response: " + response

            processed_data.append({'instruction': instruction, 'input': input_text, 'response': response})

    return processed_data

def main():
    # Load the dataset
    dataset = load_dataset("seedboxai/german_to_english_translations_v1")

    # Process both 'train' and 'test' splits of the dataset
    train_data = process_data(dataset['train'])
    test_data = process_data(dataset['test'])

    print("STARTING COMBINTAION!")
    # Create a new dataset
    new_dataset = Dataset.from_pandas(pd.DataFrame(train_data))
    print("STARTING SAVING!")
    new_dataset.save_to_disk('sandboxai_german_to_english_translations_seperated')
    print("STARTING UPLOAD.")

    new_dataset.push_to_hub("mfmezger/sandboxai_german_to_english_translations_seperated")


if __name__ == "__main__":
    main()
