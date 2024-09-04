
# ArtiGen -  for Latest Government Policy Updates

ArtiGen is an advanced article generator designed to fetch and create unique, structured articles on the latest updates from government websites. Whether it's new policies, public announcements, or regulatory changes, ArtiGen delivers up-to-date, organized, and informative content with ease.

## Table of Contents

- [Introduction](#introduction)
- [Description](#Description)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Results](#Results)
- [Contact](#Contact)
  

## Introduction

ArtiGen automates the process of generating articles on trending topics related to government updates. By scraping relevant information from various official websites, it organizes data into comprehensive articles complete with sections, tables, and images. This tool is perfect for journalists, researchers, and content creators looking to stay informed on the latest governmental developments.


## Description

Our system scrapes data from sources like MySchemes, storing it in JSON format, and then processes this data by generating embeddings and metadata. This allows ArtiGen to craft informative articles with sections, tables, and images, ensuring that the content is up-to-date and relevant.

## Installation

Follow these steps to set up ArtiGen locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/DishaGabale/artigen
   ```
2. Navigate to the project directory:
   ```bash
   cd artigen
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your Streamlit secrets for credentials:
   - Go to your Streamlit Cloud app settings.
   - Add your email and password under "Secrets" in the following format:
     ```toml
     [credentials]
     email = "your_email@example.com"
     password = "your_password"
     ```

## Usage

To use ArtiGen, follow these steps:

1. Run the Streamlit app:
   ```bash
   streamlit run src/webapp.py
   ```
2. Open your browser and go to the provided local URL.
3. Input the topic of the article in the text box, and press "Generate Article".
4. The app will display a loading GIF while generating the article.
5. View and download the generated article directly from the app interface.

## Technologies Used

- **Python**: Core programming language.
- **Streamlit**: For building the web app interface.
- **Hugchat**: For article generation
- **requests**: For handling HTTP requests during data scraping.
- **JSON**: For data storage and interchange format.
- **Embeddings**: For semantic understanding and metadata generation.

## Results
VIDEO RECORDING OF THE MODEL
https://drive.google.com/file/d/19IW999OxQQpbNe6XCVd9c81_MYPlrEjE/view?usp=sharing
Explore the output folder for screenshots of generated articles, demonstrating the application's capability to create informative and well-structured content.

## Contact

For any questions or suggestions, please contact [DishaGabale] at [gabaledisha@gmail.com].





