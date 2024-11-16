# QR Code Generator for Restaurants

A Django-based web application that helps restaurant owners create QR codes for their menu links. This tool allows users to enter their restaurant name and menu URL, generating a downloadable QR code for convenient sharing with customers.

---

## Features

- **QR Code Generation**: Quickly create QR codes based on menu URLs.
- **Stylish Interface**: User-friendly and modern design using Bootstrap.
- **Download Functionality**: Download the generated QR code as an image file.
- **Easy Navigation**: Simple workflow for generating and accessing QR codes.

---

## Technologies Used

- **Backend**: Django, Python
- **Frontend**: HTML, CSS, Bootstrap
- **QR Code Library**: `qrcode`
- **Storage**: Media folder for saving QR code images

---

## How It Works

1. **Input Information**: Enter your restaurant name and menu URL.
2. **Generate QR Code**: Click "Generate QR Code" to create a QR code.
3. **View and Download**: See the generated QR code and download it as an image.

---

## Installation

1. Clone this repository:  
   ```bash
   git clone https://github.com/ayazkhan1410/QR-Menu-Generator.git
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:  
   ```bash
   python manage.py migrate
   ```
4. Start the development server:  
   ```bash
   python manage.py runserver
   ```

---

## Usage

1. Open your browser and go to:  
   ```http
   http://127.0.0.1:8000/
   ```
2. Enter the required information.
3. Click "Generate QR Code" to see the result.
4. Download the QR code for sharing.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request to suggest improvements or report bugs.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
