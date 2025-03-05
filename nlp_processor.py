import spacy
from transformers import pipeline
from typing import List, Dict



class EdgeNLPCluster:
    def __init__(self):
        # Load language models
        self.spacy_model = spacy.load('en_core_web_sm')
        self.sentiment_model = pipeline('sentiment-analysis')

        
    def named_entity_recognition(self, text: str) -> List[Dict]:
        doc = self.spacy_model(text)
        return [
            {
                'text': ent.text, 
                'label': ent.label_
            } for ent in doc.ents
        ]


    def sentiment_analysis(self, text: str) -> Dict:
        return self.sentiment_model(text)[0]


    def process_text_batch(self, texts: List[str]) -> List[Dict]:
        results = []
        for text in texts:
            result = {
                'text': text,
                'named_entities': self.named_entity_recognition(text),
                'sentiment': self.sentiment_analysis(text)
            }
            results.append(result)

        return results

# Example usage

def main():
    nlp_cluster = EdgeNLPCluster()
    sample_texts = [
        "Oranges grow on orange trees",
        "whale breaths air for oxigen",
        "The new restaurant in town serves amazing food!",
        "The service at the store was terrible.",
        "She walked her dog in the afternoon."
    ]


    results = nlp_cluster.process_text_batch(sample_texts)
    print(results)


if __name__ == "__main__":
    main()
