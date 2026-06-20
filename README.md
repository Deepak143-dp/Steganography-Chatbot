# Steganography Chatbot

A secure web-based steganography application that allows users to hide secret messages inside images and retrieve them later through decoding. The project uses Least Significant Bit (LSB) image steganography to embed encrypted text within image pixels, ensuring private and secure communication.

## Features

- Hide secret messages inside images
- Extract hidden messages from encoded images
- User-friendly web interface
- Fast and lightweight Flask application
- Image-based secure communication
- Download encoded images instantly

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Pillow (PIL)
- LSB Steganography

## Project Structure

```bash
project/
│
├── app.py
├── steg.py
├── templates/
│   └── index.html
├── ststic/
│   └── style.css
├── uploads/
└── requirements.txt
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/Deepak143-dp/Steganography-Chatbot.git
cd Steganography-Chatbot
```

2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the application

```bash
python app.py
```

5. Open your browser

```bash
http://127.0.0.1:5000
```

## How It Works

### Encode Message

1. Enter a secret message.
2. Upload an image.
3. Click **Encode & Download**.
4. Download the encoded image.

### Decode Message

1. Upload the encoded image.
2. Click **Decode**.
3. View the hidden message.

## Security Concept

This project uses LSB (Least Significant Bit) Steganography to hide message bits inside image pixels. The hidden message remains invisible to users and can only be recovered through the decoding process.

## Future Improvements

- AES Encryption Support
- Password Protected Decoding
- Multiple Image Format Support
- Secure Key Based Message Retrieval

## Author

**Deepak Kumar**
Integrated M.Tech Cyber Security
VIT Bhopal University

## License

This project is developed for educational and research purposes.
