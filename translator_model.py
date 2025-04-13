from transformers import MarianMTModel, MarianTokenizer

class LanguageTranslator:
    def __init__(self, source_lang_code, target_lang_code):
        model_name = f'Helsinki-NLP/opus-mt-{source_lang_code}-{target_lang_code}'
        try:
            self.tokenizer = MarianTokenizer.from_pretrained(model_name)
            self.model = MarianMTModel.from_pretrained(model_name)
        except Exception as e:
            raise ValueError(f"Model for {source_lang_code}-{target_lang_code} not available.")

    def translate(self, text):
        if not text.strip():
            return ""
        inputs = self.tokenizer.prepare_seq2seq_batch([text], return_tensors="pt")
        translated = self.model.generate(**inputs)
        return self.tokenizer.batch_decode(translated, skip_special_tokens=True)[0]
