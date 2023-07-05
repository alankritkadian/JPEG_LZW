ds = {"train": train, "test": test}

def preprocess_function(examples):
    label = examples["PRODUCT_LENGTH"] 
    examples = tokenizer(examples["TITLE"], truncation=True, padding="max_length", max_length=256)
    
    # Change this to real number
    examples["label"] = float(label)
    return examples

for split in ds:
    temp = []
    for x in ds[split]:
    ds[split] = ds[split].map(preprocess_function, remove_columns=["PRODUCT_ID", "BULLET_POINTS", "DESCRIPTION", "TITLE	","PRODUCT_TYPE_ID","PRODUCT_LENGTH"])