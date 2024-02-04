from transformers import AutoModelForCausalLM, AutoTokenizer
with open ('CR/test0.txt','a') as f:
    t=f.read()

model_id = "mistralai/Mixtral-8x7B-v0.1"
tokenizer = AutoTokenizer.from_pretrained(model_id)

encoded_input = tokenizer(t)

def encode(examples):
    return tokenizer(t, truncation=True, padding='max_length')

dataset = dataset.map(encode, batched=True)


