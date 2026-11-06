from datasets import load_dataset
import pandas as pd

ds = load_dataset("openai/gsm8k", "main")

def extract_final_answer(answer_text):
    answer_split = answer_text.split("####")
    final_answer = answer_split[-1].strip()
    return final_answer.replace(",","")

def process_example(example):
    text = extract_final_answer(example["answer"])
    return {"final_answer": text}

ds = ds.map(process_example)
ds = ds.remove_columns("answer")

bad = []  
for split in ds:
    for example in ds[split]:
        final_answer = example["final_answer"]
        try:
            float(final_answer)
        except ValueError:

            bad.append((split, final_answer))


print(f"Found {len(bad)} offenders:")
print(bad[:93])
