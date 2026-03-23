import os
import requests

def fetch_and_send_news():
    # 1. መረጃ መፈለጊያ (PubMed API ለምሳሌ)
    topic = "Biotechnology"
    api_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={topic}&retmode=json&retmax=3"
    
    # 2. የቴሌግራም መለያዎች (ከ GitHub Secrets የሚመጡ)
    bot_token = os.getenv('BOT_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    
    response = requests.get(api_url).json()
    ids = response['esearchresult']['idlist']
    
    message = "🧬 **የዛሬው የባዮቴክኖሎጂ አዳዲስ ጥናቶች፦**\n\n"
    for pubmed_id in ids:
        link = f"https://pubmed.ncbi.nlm.nih.gov/{pubmed_id}/"
        message += f"• አዲስ ጥናት ተገኝቷል፦ {link}\n"

    # 3. ወደ ቴሌግራም መላክ
    send_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    requests.post(send_url, data={'chat_id': chat_id, 'text': message, 'parse_mode': 'Markdown'})

if __name__ == "__main__":
    fetch_and_send_news()
