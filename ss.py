import time
import pandas as pd
import json
import tkinter as tk
from tkinter import filedialog, messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def search_word_in_website(search_term):
    """جستجو و استخراج نتایج از وب‌سایت."""

    # تنظیمات ChromeDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # برای اجرا در پس‌زمینه
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # مسیر ChromeDriver
    service = Service(r"C:\path\to\chromedriver.exe")  # مسیر صحیح ChromeDriver را وارد کنید
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # باز کردن وب‌سایت
        driver.get("https://der-artikel.de/der/Finder.html")

        # پیدا کردن فیلد جستجو و تایپ کلمه
        search_box = driver.find_element(By.ID, 'word')
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)

        # صبر کردن برای بارگذاری نتایج
        time.sleep(10)  # افزایش زمان برای بارگذاری نتایج

        # استخراج نتایج
        results = {}
        rows = driver.find_elements(By.CSS_SELECTOR, '.table tbody tr')

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            if len(cells) >= 3:
                type_of_case = cells[0].text.strip()
                singular = cells[1].text.strip()
                plural = cells[2].text.strip()
                if type_of_case in ['NOMINATIV', 'GENITIV', 'DATIV', 'AKKUSATIV']:
                    results[type_of_case] = {
                        'Singular': singular,
                        'Plural': plural
                    }

        return results
    finally:
        driver.quit()  # بستن مرورگر

def process_words_from_excel(input_excel_path, output_excel_path, dict_file_path, status_label):
    """خواندن کلمات از فایل اکسل و ذخیره نتایج جستجو در فایل اکسل و به صورت دیکشنری در نوت پد."""

    # خواندن داده‌ها از فایل اکسل بدون نام ستون‌ها
    df = pd.read_excel(input_excel_path, header=None)  # header=None به این معنی است که اکسل بدون نام ستون است

    # ستون اول (ستون 0) را به عنوان لیست کلمات انتخاب کنید
    words = df.iloc[:, 0]  # انتخاب تمام ردیف‌ها از ستون اول

    # ایجاد یک لیست برای ذخیره نتایج
    results_list = []
    results_dict = {}

    # تعداد کل کلمات
    total_words = len(words)

    # پردازش هر کلمه
    for idx, word in enumerate(words):
        status_label.config(text=f"در حال پردازش کلمه {idx + 1} از {total_words}")
        status_label.update()  # به‌روزرسانی وضعیت نمایش

        search_results = search_word_in_website(word)

        # اضافه کردن نتایج به لیست
        for case, forms in search_results.items():
            results_list.append({
                'Word': word,
                'Case': case,
                'Singular': forms['Singular'],
                'Plural': forms['Plural']
            })

        # اضافه کردن نتایج به دیکشنری
        results_dict[word] = search_results

    # تبدیل لیست نتایج به DataFrame
    results_df = pd.DataFrame(results_list)

    # ذخیره نتایج در فایل اکسل جدید
    results_df.to_excel(output_excel_path, index=False)

    # ذخیره دیکشنری پایتون در فایل متنی به صورت JSON
    with open(dict_file_path, 'w', encoding='utf-8') as dict_file:
        json.dump(results_dict, dict_file, ensure_ascii=False, indent=4)

    status_label.config(text="پردازش با موفقیت انجام شد.")

def browse_file(entry):
    """باز کردن پنجره انتخاب فایل و قرار دادن مسیر آن در فیلد ورودی."""
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

def browse_save_location(entry):
    """باز کردن پنجره انتخاب محل ذخیره فایل و قرار دادن مسیر آن در فیلد ورودی."""
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

def start_processing(input_entry, output_entry, dict_entry, status_label):
    """شروع پردازش فایل و نمایش پیام نتیجه."""
    input_excel = input_entry.get()
    output_excel = output_entry.get()
    dict_file = dict_entry.get()

    if not input_excel or not output_excel or not dict_file:
        messagebox.showerror("Error", "لطفاً تمام مسیرها را وارد کنید.")
        return

    try:
        process_words_from_excel(input_excel, output_excel, dict_file, status_label)
        messagebox.showinfo("Success", "پردازش با موفقیت انجام شد.")
    except Exception as e:
        messagebox.showerror("Error", f"خطا در هنگام پردازش: {e}")

# رابط گرافیکی با استفاده از tkinter
root = tk.Tk()
root.title("جستجو و استخراج کلمات آلمانی")

# فیلد ورودی برای انتخاب فایل اکسل ورودی
tk.Label(root, text="فایل اکسل ورودی:").grid(row=0, column=0, padx=10, pady=10)
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="انتخاب فایل", command=lambda: browse_file(input_entry)).grid(row=0, column=2, padx=10, pady=10)

# فیلد ورودی برای انتخاب محل ذخیره فایل اکسل خروجی
tk.Label(root, text="محل ذخیره فایل اکسل خروجی:").grid(row=1, column=0, padx=10, pady=10)
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="انتخاب محل", command=lambda: browse_save_location(output_entry)).grid(row=1, column=2, padx=10, pady=10)

# فیلد ورودی برای انتخاب محل ذخیره فایل دیکشنری
tk.Label(root, text="محل ذخیره فایل دیکشنری:").grid(row=2, column=0, padx=10, pady=10)
dict_entry = tk.Entry(root, width=50)
dict_entry.grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="انتخاب محل", command=lambda: browse_save_location(dict_entry)).grid(row=2, column=2, padx=10, pady=10)

# دکمه شروع پردازش
tk.Button(root, text="شروع پردازش", command=lambda: start_processing(input_entry, output_entry, dict_entry, status_label)).grid(row=3, column=0, columnspan=3, pady=20)

# برچسب برای نمایش وضعیت پردازش
status_label = tk.Label(root, text="", fg="blue")
status_label.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()
