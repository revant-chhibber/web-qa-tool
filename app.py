from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict

app = Flask(__name__)

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Store ingested content
content_db = {}

def ingest_url(url):
    """Scrape and process content from a URL"""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract text from paragraphs
        text = ' '.join(p.get_text() for p in soup.find_all('p'))
        
        # Process text into sentences and create simple index
        sentences = sent_tokenize(text)
        word_index = defaultdict(list)
        
        stop_words = set(stopwords.words('english'))
        
        for i, sentence in enumerate(sentences):
            words = [w.lower() for w in word_tokenize(sentence) if w.isalnum() and w.lower() not in stop_words]
            for word in words:
                word_index[word].append(i)
        
        return {
            'sentences': sentences,
            'index': word_index,
            'raw_text': text
        }
    except Exception as e:
        return {'error': str(e)}

def answer_question(question, content):
    """Generate answer based on ingested content"""
    if 'error' in content:
        return f"Error processing content: {content['error']}"
    if not content['sentences']:
        return "No content available to answer the question."
    
    # Simple keyword-based matching
    question_words = [w.lower() for w in word_tokenize(question) if w.isalnum()]
    sentences = content['sentences']
    index = content['index']
    
    # Find relevant sentences
    relevant_sentences = set()
    for word in question_words:
        if word in index:
            relevant_sentences.update(index[word])
    
    if not relevant_sentences:
        return "No relevant information found."
    
    # Return the most relevant sentence(s)
    answer_sentences = [sentences[i] for i in sorted(list(relevant_sentences))[:2]]  # Limit to 2 sentences
    return ' '.join(answer_sentences)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ingest', methods=['POST'])
def ingest():
    urls = request.json.get('urls', [])
    global content_db
    content_db = {}
    for url in urls:
        content_db[url] = ingest_url(url)
    return jsonify({'status': 'success', 'ingested': list(content_db.keys())})

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json.get('question', '')
    answers = {}
    for url, content in content_db.items():
        answers[url] = answer_question(question, content)
    return jsonify({'answers': answers})

if __name__ == '__main__':
    app.run(debug=True)