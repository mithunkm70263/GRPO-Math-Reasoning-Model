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

def build_prompt(question):
    return f"""Solve the math problem below. First think through it step by step.
Then write your final answer inside <answer></answer> tags.
Put only the number inside the tags: no units, no $ sign, no commas, no words.

Example:
Question: A shop sells 3 pens at 4 dollars each. How much do the pens cost in total?
Reasoning: 3 pens at 4 dollars each is 3 x 4 = 12.
<answer>12</answer>

Question: {question}
"""

print(build_prompt(ds["train"][0]["question"]))