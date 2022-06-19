from gtts import gTTS
import pdfplumber
from pathlib import Path

def pdf2mp3(file_path='test.pdf', language='en'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        # return 'File exists!'

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n','')

        my_audio = gTTS(text=text, lang=language, slow='True')
        # file_name = Path(file_path).stem
        
        file_name = '.'.join(file_path.split('.')[:2])
    
        my_audio.save(f'{file_name}.mp3')
        return f'[+] file {file_name}.mp3 saved successfully!\n---Bye!---'

    else:
        return 'No File'

def main():
    print(pdf2mp3('./pdf_files/en1.pdf','en'))

if __name__ == '__main__':
    main()