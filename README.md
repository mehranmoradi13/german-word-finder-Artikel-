# German Word Search Application
# برنامه جستجوی کلمات آلمانی
# Deutsche Wort-Suchanwendung

## Overview
## معرفی
## Übersicht

This Python application provides a graphical user interface (GUI) for searching and processing German words using the `Selenium` and `Tkinter` libraries. The application allows users to search for German words on a specific website and store the results in both Excel and JSON formats.

این برنامه پایتون یک رابط کاربری گرافیکی (GUI) برای جستجو و پردازش کلمات آلمانی با استفاده از کتابخانه‌های `Selenium` و `Tkinter` ارائه می‌دهد. این برنامه به کاربران امکان می‌دهد تا کلمات آلمانی را در یک وب‌سایت خاص جستجو کرده و نتایج را در قالب‌های Excel و JSON ذخیره کنند.

Dieses Python-Programm bietet eine grafische Benutzeroberfläche (GUI) zur Suche und Verarbeitung deutscher Wörter mit den Bibliotheken `Selenium` und `Tkinter`. Die Anwendung ermöglicht es den Benutzern, nach deutschen Wörtern auf einer bestimmten Website zu suchen und die Ergebnisse sowohl im Excel- als auch im JSON-Format zu speichern.

## Features
## ویژگی‌ها
## Funktionen

- **Graphical User Interface (GUI):** Built with Tkinter for an intuitive user experience.
- **Web Scraping:** Uses Selenium to interact with a web-based German word dictionary.
- **Data Storage:** Results are saved in Excel and JSON formats.
- **Real-time Status Updates:** Displays processing status in the GUI.

- **رابط کاربری گرافیکی (GUI):** ساخته شده با Tkinter برای تجربه کاربری شهودی.
- **جستجو در وب:** استفاده از Selenium برای تعامل با دیکشنری آنلاین کلمات آلمانی.
- **ذخیره‌سازی داده‌ها:** نتایج در قالب‌های Excel و JSON ذخیره می‌شود.
- **به‌روزرسانی وضعیت به‌طور همزمان:** نمایش وضعیت پردازش در GUI.

- **Grafische Benutzeroberfläche (GUI):** Erbaut mit Tkinter für eine intuitive Benutzererfahrung.
- **Web Scraping:** Verwendet Selenium, um mit einem webbasierten deutschen Wörterbuch zu interagieren.
- **Datenablage:** Ergebnisse werden im Excel- und JSON-Format gespeichert.
- **Echtzeit-Statusaktualisierungen:** Zeigt den Verarbeitungsstatus in der GUI an.

## Requirements
## نیازمندی‌ها
## Anforderungen

- Python 3.12 or later
- `pandas`
- `openpyxl`
- `selenium`
- `tkinter`
- ChromeDriver (compatible with your version of Chrome)

- پایتون 3.12 یا بالاتر
- `pandas`
- `openpyxl`
- `selenium`
- `tkinter`
- ChromeDriver (سازگار با نسخه Chrome شما)

- Python 3.12 oder später
- `pandas`
- `openpyxl`
- `selenium`
- `tkinter`
- ChromeDriver (kompatibel mit Ihrer Version von Chrome)

## Installation
## نصب
## Installation

### 1. Clone the Repository
### 1. کلون کردن مخزن
### 1. Repository klonen

```bash
git clone https://github.com/mehranmoradi13


2. Install Python Packages
2. نصب پکیج‌های پایتون
2. Python-Pakete installieren

pip install pandas openpyxl selenium

3. Download ChromeDriver
3. دانلود ChromeDriver
3. ChromeDriver herunterladen
Download the ChromeDriver executable from ChromeDriver Downloads and place it in the same directory as the Python script or add its path to the search_word_in_website function in ss.py.

دانلود فایل اجرایی ChromeDriver از ChromeDriver Downloads و قرار دادن آن در همان دایرکتوری با اسکریپت پایتون یا اضافه کردن مسیر آن به تابع search_word_in_website در ss.py.

Laden Sie die ChromeDriver-Binärdatei von ChromeDriver Downloads herunter und platzieren Sie sie im gleichen Verzeichnis wie das Python-Skript oder fügen Sie ihren Pfad zur Funktion search_word_in_website in ss.py hinzu.

Usage
نحوه استفاده
Verwendung
Run the Application

1. اجرای برنامه
1. Die Anwendung ausführen
Execute the Python script to open the GUI:

python ss.py

Select Input Files

2. انتخاب فایل‌های ورودی
2. Eingabedateien auswählen
Input Excel File: Choose an Excel file that contains the list of German words (one word per row).

Output Excel File: Specify where to save the Excel file with the search results.

JSON Dictionary File: Specify where to save the JSON file containing the search results in dictionary format.

فایل اکسل ورودی: انتخاب یک فایل اکسل که شامل لیست کلمات آلمانی است (یک کلمه در هر ردیف).

فایل اکسل خروجی: مشخص کردن محل ذخیره فایل اکسل با نتایج جستجو.

فایل دیکشنری JSON: مشخص کردن محل ذخیره فایل JSON حاوی نتایج جستجو به صورت دیکشنری.

Eingabedatei Excel: Wählen Sie eine Excel-Datei aus, die die Liste der deutschen Wörter enthält (ein Wort pro Zeile).

Ausgabedatei Excel: Geben Sie an, wo die Excel-Datei mit den Suchergebnissen gespeichert werden soll.

JSON-Wörterbuchdatei: Geben Sie an, wo die JSON-Datei gespeichert werden soll, die die Suchergebnisse im Wörterbuchformat enthält.

Start Processing

3. شروع پردازش
3. Verarbeitung starten
Click on "Start Processing" to begin the word search and processing. The status label will update to show the current progress.

روی "شروع پردازش" کلیک کنید تا جستجو و پردازش کلمات آغاز شود. برچسب وضعیت به‌روزرسانی خواهد شد تا پیشرفت فعلی را نشان دهد.

Klicken Sie auf „Verarbeitung starten“, um die Suche und Verarbeitung von Wörtern zu beginnen. Das Statusetikett wird aktualisiert, um den aktuellen Fortschritt anzuzeigen.

Code Structure
ساختار کد
Code-Struktur
ss.py: Main Python script that contains the logic for web scraping, data processing, and GUI.

chromedriver.exe: ChromeDriver executable required for Selenium (ensure it's compatible with your Chrome version).

ss.py: اسکریپت اصلی پایتون که شامل منطق جستجو در وب، پردازش داده‌ها و GUI است.

chromedriver.exe: فایل اجرایی ChromeDriver مورد نیاز برای Selenium (مطمئن شوید که با نسخه Chrome شما سازگار است).

ss.py: Haupt-Python-Skript, das die Logik für Web-Scraping, Datenverarbeitung und GUI enthält.

chromedriver.exe: Ausführbare ChromeDriver-Datei, die für Selenium erforderlich ist (stellen Sie sicher, dass sie mit Ihrer Chrome-Version kompatibel ist).

Contributing
مشارکت
Mitwirken
Feel free to fork this repository and submit pull requests for improvements or bug fixes. Please follow the standard contribution guidelines.

لطفاً به راحتی این مخزن را فورک کرده و درخواست‌های کشش برای بهبودها یا رفع اشکالات ارسال کنید. لطفاً از دستورالعمل‌های استاندارد مشارکت پیروی کنید.

Fühlen Sie sich frei, dieses Repository zu forken und Pull-Requests für Verbesserungen oder Fehlerbehebungen einzureichen. Bitte folgen Sie den Standardbeitragsrichtlinien.

License
مجوز
Lizenz
This project is licensed under the MIT License - see the LICENSE file for details.

این پروژه تحت مجوز MIT منتشر شده است - جزئیات در فایل LICENSE آمده است.

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die LICENSE-Datei für Details.

Acknowledgments
قدردانی
Danksagungen
Selenium: For web scraping capabilities.

Tkinter: For creating the graphical user interface.

Pandas: For handling data in Excel and JSON formats.

Selenium: برای قابلیت‌های جستجو در وب.

Tkinter: برای ایجاد رابط کاربری گرافیکی.

Pandas: برای مدیریت داده‌ها در قالب‌های Excel و JSON.

Selenium: Für Web-Scraping-Funktionen.

Tkinter: Für die Erstellung der grafischen Benutzeroberfläche.

Pandas: Für die Verarbeitung von Daten in Excel- und JSON-Formaten.

Contact
تماس
Kontakt
For any questions or issues, please contact m.mehran90@Live.com & https://www.linkedin.com/in/mehranmoradi

برای هر گونه سوال یا مشکل، لطفاً با your-email@example.com تماس بگیرید.

Bei Fragen oder Problemen wenden Sie sich bitte an m.mehran90@Live.com & https://www.linkedin.com/in/mehranmoradi

