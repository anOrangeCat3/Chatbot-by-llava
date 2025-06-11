import random
import pandas as pd
from gpt4all import GPT4All
from tqdm import tqdm


# Load dataset
def load_local_boolq_dataset(filepath):
    df = pd.read_parquet(filepath)
    return df.to_dict(orient="records")


# Samples
def select_random_samples(validation_set, seed, sample_size=500):
    random.seed(seed)
    return random.sample(validation_set, sample_size)


# Infer function
def infer_gpt4all(model, question, passage):
    input_text = f"Question: {question}\nPassage: {passage}\nAnswer (yes or no):"

    # Generate answers
    generated_text = model.generate(input_text)
    if "yes" in generated_text.lower():
        return True
    elif "no" in generated_text.lower():
        return False
    else:
        return None


# Evaluation of accuracy
def evaluate_boolq(model, validation_samples):
    correct = 0
    total = 0

    for sample in tqdm(validation_samples):
        question = sample['question']
        passage = sample['passage']
        true_answer = sample['answer']  # 1 = True, 0 = False

        # Infer
        predicted_answer = infer_gpt4all(model, question, passage)
        true_answer = True if true_answer == 1 else False

        # Count on correct ones
        if predicted_answer is not None:
            total += 1
            if predicted_answer == true_answer:
                correct += 1

    # Calculate accuracy
    accuracy = correct / total if total > 0 else 0
    return accuracy


def main():
    # Model
    gpt = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")

    filepath = "validation-00000-of-00001.parquet"
    validation_set = load_local_boolq_dataset(filepath)

    # Matriculation Number
    matr_num = 243

    selected_samples = select_random_samples(validation_set, matr_num)

    accuracy = evaluate_boolq(gpt, selected_samples)
    print(f"Accuracy on 500 selected samples of BoolQ validation set: {accuracy * 100:.2f}%")


if __name__ == "__main__":
    main()
