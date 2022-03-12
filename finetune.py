from transformers import AutoTokenizer, AutoModel
import torch.nn.functional as F

checkpoint = "distilbert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)

raw_inputs = [
    "I've been waiting for a HuggingFace course my whole life.",
    "I hate this so much!",
]
inputs = tokenizer(raw_inputs, padding=True, truncation=True, return_tensors="pt")

model = AutoModel.from_pretrained(checkpoint)

outputs = model(**inputs)
print(outputs)
