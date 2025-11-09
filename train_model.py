from datasets import load_dataset
from transformers import (AutoTokenizer, AutoModelForSequenceClassification,
                          Trainer, TrainingArguments, DataCollatorWithPadding)
import numpy as np
import os

MODEL_NAME = "distilbert-base-uncased"
OUTPUT_DIR = "model"  # saved model path

def tokenize_fn(batch, tokenizer):
    return tokenizer(batch["text"], truncation=True, padding=False)

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=-1)
    acc = (preds == labels).astype(np.float32).mean().item()
    return {"accuracy": acc}

def main():
    print("Loading IMDB dataset (small) ...")
    dataset = load_dataset("imdb")
    # optional: reduce size for quick demo
    # dataset['train'] = dataset['train'].shuffle(seed=42).select(range(4000))
    # dataset['test']  = dataset['test'].shuffle(seed=42).select(range(1000))

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    tokenized = dataset.map(lambda batch: tokenize_fn(batch, tokenizer), batched=True)

    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=2)

    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

    training_args = TrainingArguments(
        output_dir="./results",
        evaluation_strategy="epoch",
        save_strategy="epoch",
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        num_train_epochs=1,        # set to 2-3 for better perf
        weight_decay=0.01,
        logging_steps=50,
        push_to_hub=False,
        load_best_model_at_end=True,
        metric_for_best_model="accuracy",
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized["train"],
        eval_dataset=tokenized["test"],
        tokenizer=tokenizer,
        data_collator=data_collator,
        compute_metrics=compute_metrics,
    )

    print("Starting training ...")
    trainer.train()

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Saving model to {OUTPUT_DIR} ...")
    model.save_pretrained(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)
    print("Saved.")

if __name__ == "__main__":
    main()
