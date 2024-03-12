from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search', methods=["POST"])
def search():
    person_name = request.form['person_name']
    images = search_images(person_name)
    return render_template('result.html', images = images)

def search_images(person_name):
    # Search for images using the person's name
    search_query = f"{person_name} 사진"
    url = f"https://www.google.com/search?q={search_query}&tbm=isch"

    # Send HTTP request and get the response
    header = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    # Parse the response using BeautifulSoup
    soup = BeautifulSoup(response.txt, 'html_parser')

    # Extract image URLs
    images = []
    for img in soup.find_all('img'):
        images.append(img.get('src'))

    # Download images
    download_images(images, person_name)

    return images

def download_images(image_urls, person_name):
    # Create a directory to save images
    os.makedirs(f"static/{person_name}", exist_ok=True)

    # Download and save images
    for i, url in enumerate(image_urls):
        try:
            response = requests.get(url)
            with open(f"static/{person_name}/{person_name}_{i+1}.jpg", 'wb') as f:
                f.write(response.content)
        except Exception as e:
            print(f"Error downloading image {url}: {e}")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
    