from transformers import AutoTokenizer, AutoModelForCausalLM

class TextGenerationModel:
    def __init__(self):
        self.model_name = "NousResearch/DeepHermes-3-Llama-3-8B-Preview"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)

    def generate_text(self, prompt, max_length=100):
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(inputs["input_ids"], max_length=max_length)
        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return generated_text