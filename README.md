# NLP Cluster Project

## Natural Language Processing System (Future Edge Computing Cluster)

A NLP system currently running on a single device with plans to evolve into a distributed edge computing cluster for scalable text processing.

## Project Overview

This project implements a Natural Language Processing (NLP) system that currently runs on a single laptop but is designed with the architecture to eventually support distributed computing across multiple edge devices. It uses modern NLP libraries to process text data for sentiment analysis and named entity recognition.

### Current Capabilities

- **Named Entity Recognition**: Identify and classify named entities in text
- **Sentiment Analysis**: Determine the emotional tone of text
- **Local Processing**: Currently running on a single laptop environment

### Future Goals

- **Distributed Processing**: Scale to multiple devices for parallel text processing
- **Edge Computing Implementation**: Deploy on Raspberry Pi or similar edge devices
- **Containerized Architecture**: Implement Docker-based deployment for scalability

## Current Status & Performance

- **Environment**: Currently running on a single HP laptop (not yet distributed)
- **Processing Time**: ~13 seconds for the sample text batch
- **Sentiment Analysis Model**: The current model shows some inaccuracies in sentiment detection
  - Example: "She walked her dog in the afternoon" incorrectly classified as negative sentiment
- **Docker Implementation**: In progress (not yet running properly)
- **Cluster Architecture**: Planned for future implementation

## Installation

### Prerequisites

- Python 3.10+
- Docker (for future containerized deployment)
- 12GB RAM recommended

### Setup

```bash
# Clone the repository
git clone https://github.com/saeedrila/nlp-cluster-project.git
cd nlp-cluster-project

# Create virtual environment
python -m venv myenv
source myenv/bin/activate   # On Windows: myenv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download required models
python -m spacy download en_core_web_sm
```

## Usage

### Running Locally

```bash
# Run the NLP processor
python -m src.nlp_processor
```

### Sample Output

```
Starting NLP Processor...
Loading sentiment analysis model...
Device set to use cpu
Model loaded successfully!
[
  {
    'text': 'Oranges grow on orange trees', 
    'named_entities': [{'text': 'Oranges', 'label': 'ORG'}], 
    'sentiment': {'label': 'POSITIVE', 'score': 0.9969203472137451}
  },
  {
    'text': 'whale breaths air for oxigen', 
    'named_entities': [], 
    'sentiment': {'label': 'POSITIVE', 'score': 0.8638830184936523}
  },
  {
    'text': 'The new restaurant in town serves amazing food!', 
    'named_entities': [], 
    'sentiment': {'label': 'POSITIVE', 'score': 0.9998804330825806}
  },
  {
    'text': 'The service at the store was terrible.', 
    'named_entities': [], 
    'sentiment': {'label': 'NEGATIVE', 'score': 0.9996034502983093}
  },
  {
    'text': 'She walked her dog in the afternoon.', 
    'named_entities': [], 
    'sentiment': {'label': 'NEGATIVE', 'score': 0.6085323095321655}
  }
]
```

## Project Structure

```
nlp-cluster-project/
├── src/
│   ├── nlp_processor.py
│   └── __pycache__/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Technical Details

### Models Used

- **Sentiment Analysis**: Hugging Face Transformers pipeline with default sentiment model
- **Named Entity Recognition**: spaCy 'en_core_web_sm' model

### Current Performance Metrics

| Metric | Value |
|--------|-------|
| Average processing time | 13.083s |
| CPU time | 7.594s |
| System time | 0.679s |

## Development Roadmap

### Phase 1: Single Machine Implementation (Current)
- [x] Implement basic NLP functionality
- [x] Set up sentiment analysis and NER
- [ ] Fix sentiment analysis accuracy issues
- [ ] Fix NER issues
- [ ] Implement a more accurate sentiment model
- [ ] Add unit tests

### Phase 2: Containerization
- [ ] Fix Docker deployment
- [ ] Test containerized performance
- [ ] Optimize container resource usage

### Phase 3: Distributed Architecture (Future)
- [ ] Set up multiple worker nodes
- [ ] Implement message queue for task distribution
- [ ] Create load balancing mechanism
- [ ] Deploy on edge devices (Raspberry Pi)

### Phase 4: Advanced Features
- [ ] Implement additional NLP tasks (summarization, question answering)
- [ ] Add REST API for model serving
- [ ] Add GPU support for faster inference
- [ ] Implement monitoring and logging

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Hugging Face Transformers team for their incredible NLP models
- spaCy for their efficient NLP pipeline

## Contact

Saeed Rila - [saeedrila@gmail.com](mailto:saeedrila@gmail.com)  
Project Link: [https://github.com/saeedrila/nlp-cluster-project](https://github.com/saeedrila/nlp-cluster-project)