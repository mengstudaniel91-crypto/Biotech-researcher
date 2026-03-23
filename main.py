import requests

def fetch_biotech_news():
    # ለምሳሌ ስለ 'CRISPR' ወይም 'Vaccine' መረጃ መፈለግ ቢፈልጉ
    topic = "Biotechnology"
    print(f"ለ ዳንኤል ስለ {topic} አዳዲስ መረጃዎችን እየፈለግኩ ነው...")
    
    # ለጊዜው መረጃው ያለበትን ሊንክ እናሳይ
    search_url = f"https://pubmed.ncbi.nlm.nih.gov/?term={topic}"
    print(f"የጥናቶቹን ዝርዝር እዚህ ያገኙታል፦ {search_url}")

if __name__ == "__main__":
    fetch_biotech_news()
