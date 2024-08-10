from transformers import pipeline

# Load pre-trained BERT model for classification
classifier = pipeline('text-classification')

def identify_cyber_platform(text):
    result = classifier(text)
    return result[0]['label'] == 'LABEL_1'  # Adjust this label as needed

if __name__ == "__main__":
    text = "Latest cyber incidents reported in Indian cyberspace."
    if identify_cyber_platform(text):
        print("This platform is relevant for cyber incident tracking.")
    else:
        print("This platform is not relevant.")