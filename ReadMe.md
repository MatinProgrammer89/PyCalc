# 🧮 MatinCalculator

**A modern desktop calculator application built with Python and Qt Designer.**

**یک برنامه ماشین حساب دسکتاپ با رابط کاربری گرافیکی، ساخته‌شده با Python و Qt Designer.**

---

## 🇮🇷 فارسی

### 📌 معرفی پروژه

**MatinCalculator** یک برنامه ماشین حساب دسکتاپ است که با استفاده از **Python** توسعه داده شده و رابط کاربری آن با **Qt Designer** طراحی شده است.

ساختار پروژه به گونه‌ای طراحی شده که بخش **منطق محاسبات، رابط کاربری و تاریخچه محاسبات** از یکدیگر جدا باشند تا کد خواناتر، قابل توسعه‌تر و تست‌پذیرتر باشد.

این پروژه همچنین دارای فایل اجرایی مستقل و فایل نصب ویندوز است که با استفاده از **PyInstaller** و **Inno Setup** ساخته شده‌اند.

### ✨ امکانات

* ➕ انجام عملیات جمع
* ➖ انجام عملیات تفریق
* ✖️ انجام عملیات ضرب
* ➗ انجام عملیات تقسیم
* 🧮 رابط کاربری گرافیکی
* 📜 پنجره تاریخچه محاسبات
* 🎨 طراحی رابط کاربری با Qt Designer
* 🧩 جداسازی منطق محاسبات از رابط کاربری
* 🪟 نسخه اجرایی برای Windows
* 📦 فایل نصب مستقل
* 🎯 ساختار منظم و قابل توسعه

### 🛠️ تکنولوژی‌های استفاده‌شده

| تکنولوژی       | کاربرد                      |
| -------------- | --------------------------- |
| 🐍 Python      | زبان برنامه‌نویسی اصلی      |
| 🎨 Qt Designer | طراحی رابط کاربری           |
| 🖥️ PyQt       | ایجاد و مدیریت رابط گرافیکی |
| 📦 PyInstaller | ساخت فایل اجرایی            |
| 💿 Inno Setup  | ساخت فایل نصب ویندوز        |

### 📂 ساختار پروژه

```text
MatinCalculator/
│
├── main.py
│   └── فایل اصلی اجرای برنامه
│
├── logic.py
│   └── توابع محاسباتی جداشده برای خوانایی و تست‌پذیری
│
├── ui/
│   ├── main.ui
│   │   └── فرم اصلی ماشین حساب
│   │
│   └── history.ui
│       └── فرم پنجره تاریخچه
│
├── icon/
│   ├── main_icon.ico
│   │   └── آیکون پنجره اصلی و فایل نصب
│   │
│   └── history_icon.ico
│       └── آیکون پنجره تاریخچه
│
├── setup.iss
│   └── اسکریپت نصب با Inno Setup
│
├── ReadMe.md
│   └── توضیحات پروژه، نحوه اجرا و نصب
│
├── dist/
│   └── main.exe
│       └── فایل اجرایی ساخته‌شده با PyInstaller
│
└── output/
    └── MatinCalculatorSetup.exe
        └── فایل نصب ساخته‌شده با Inno Setup
```

### 🚀 اجرای پروژه از سورس

ابتدا repository را Clone کنید:

```bash
git clone https://github.com/USERNAME/MatinCalculator.git
```

وارد پوشه پروژه شوید:

```bash
cd MatinCalculator
```

سپس وابستگی‌های موردنیاز را نصب کنید:

```bash
pip install -r requirements.txt
```

برنامه را اجرا کنید:

```bash
python main.py
```

> در صورتی که فایل `requirements.txt` در پروژه وجود ندارد، می‌توانید آن را بر اساس کتابخانه‌های استفاده‌شده در پروژه اضافه کنید.

### 🪟 اجرای نسخه آماده

اگر نمی‌خواهید Python و وابستگی‌های پروژه را نصب کنید، می‌توانید از فایل نصب آماده استفاده کنید:

```text
output/MatinCalculatorSetup.exe
```

همچنین نسخه اجرایی برنامه در مسیر زیر قرار دارد:

```text
dist/main.exe
```

### 📦 ساخت فایل اجرایی

برای ساخت نسخه اجرایی با **PyInstaller** می‌توانید از دستور زیر استفاده کنید:

```bash
pyinstaller --onefile --windowed main.py
```

پس از Build، فایل اجرایی در پوشه `dist/` قرار می‌گیرد.

### 💿 ساخت فایل نصب

فایل:

```text
setup.iss
```

برای ساخت Installer با **Inno Setup** استفاده می‌شود.

پس از اجرای اسکریپت نصب، فایل نصب نهایی در پوشه `output/` قرار می‌گیرد:

```text
MatinCalculatorSetup.exe
```

### 🖼️ پیش‌نمایش

برای نمایش ظاهر برنامه در GitHub، پیشنهاد می‌شود چند Screenshot از برنامه اضافه کنید:

```markdown
![MatinCalculator](screenshots/main.png)
```

همچنین می‌توانید تصویر پنجره تاریخچه را اضافه کنید:

```markdown
![History Window](screenshots/history.png)
```

### 🎯 هدف پروژه

این پروژه با هدف تمرین و پیاده‌سازی مفاهیم زیر ساخته شده است:

* برنامه‌نویسی Python
* توسعه برنامه‌های Desktop
* طراحی رابط کاربری با Qt Designer
* جداسازی Logic از UI
* مدیریت رویدادهای رابط کاربری
* ایجاد سیستم تاریخچه محاسبات
* ساخت فایل اجرایی با PyInstaller
* ساخت Installer برای Windows با Inno Setup
* ایجاد ساختار تمیز و قابل توسعه برای پروژه

### 🔮 قابلیت‌های آینده

* [ ] اضافه کردن حالت Scientific Calculator
* [ ] ذخیره دائمی تاریخچه محاسبات
* [ ] پشتیبانی کامل از صفحه‌کلید
* [ ] اضافه کردن Dark Mode
* [ ] اضافه کردن توابع ریاضی بیشتر
* [ ] امکان پاک کردن تاریخچه
* [ ] بهبود مدیریت خطاها
* [ ] اضافه کردن تست‌های واحد برای `logic.py`

---

# 🇬🇧 English

## 📌 About

**MatinCalculator** is a desktop calculator application developed with **Python**, with its graphical user interface designed using **Qt Designer**.

The project is structured to keep the **calculation logic, user interface, and calculation history** separated, making the code cleaner, easier to maintain, test, and extend.

The project also provides a standalone Windows executable and an installer created using **PyInstaller** and **Inno Setup**.

## ✨ Features

* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division
* 🧮 Graphical User Interface
* 📜 Calculation history window
* 🎨 UI designed with Qt Designer
* 🧩 Separated calculation logic
* 🪟 Windows executable
* 📦 Standalone Windows installer
* 🎯 Clean and maintainable project structure

## 🛠️ Technologies

| Technology     | Purpose                        |
| -------------- | ------------------------------ |
| 🐍 Python      | Main programming language      |
| 🎨 Qt Designer | User interface design          |
| 🖥️ PyQt       | GUI development                |
| 📦 PyInstaller | Creating the executable        |
| 💿 Inno Setup  | Creating the Windows installer |

## 📂 Project Structure

```text
MatinCalculator/
│
├── main.py
│   └── Main application entry point
│
├── logic.py
│   └── Separated calculation functions
│
├── ui/
│   ├── main.ui
│   │   └── Main calculator interface
│   │
│   └── history.ui
│       └── Calculation history window
│
├── icon/
│   ├── main_icon.ico
│   │   └── Main window and installer icon
│   │
│   └── history_icon.ico
│       └── History window icon
│
├── setup.iss
│   └── Inno Setup installation script
│
├── ReadMe.md
│   └── Project documentation
│
├── dist/
│   └── main.exe
│       └── Executable generated with PyInstaller
│
└── output/
    └── MatinCalculatorSetup.exe
        └── Windows installer generated with Inno Setup
```

## 🚀 Run from Source

Clone the repository:

```bash
git clone https://github.com/USERNAME/MatinCalculator.git
```

Navigate to the project directory:

```bash
cd MatinCalculator
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

> If the project does not currently contain a `requirements.txt` file, you can create one based on the Python packages used by the project.

## 🪟 Run the Ready-to-Use Version

If you don't want to install Python and the required dependencies, you can use the pre-built Windows installer:

```text
output/MatinCalculatorSetup.exe
```

A standalone executable is also available at:

```text
dist/main.exe
```

## 📦 Building the Executable

The application can be packaged using **PyInstaller**.

For example:

```bash
pyinstaller --onefile --windowed main.py
```

After building, the executable will be generated inside the `dist/` directory.

## 💿 Creating the Installer

The file:

```text
setup.iss
```

is the **Inno Setup** script used to create the Windows installer.

After compiling the script with Inno Setup, the final installer will be available in:

```text
output/MatinCalculatorSetup.exe
```

## 🖼️ Screenshots

You can add screenshots of the application to showcase the interface:

```markdown
![MatinCalculator](screenshots/main.png)
```

You can also add a screenshot of the history window:

```markdown
![History Window](screenshots/history.png)
```

## 🎯 Project Goals

This project was created to practice and demonstrate:

* Python programming
* Desktop application development
* GUI design with Qt Designer
* Separation of UI and application logic
* Event handling
* Calculation history management
* Creating executables with PyInstaller
* Creating Windows installers with Inno Setup
* Building a clean and maintainable project structure

## 🔮 Future Improvements

* [ ] Scientific calculator mode
* [ ] Persistent calculation history
* [ ] Full keyboard support
* [ ] Dark mode
* [ ] Additional mathematical functions
* [ ] Clear history option
* [ ] Improved error handling
* [ ] Unit tests for `logic.py`

---

## 👨‍💻 Author

**Matin**

If you find this project useful, consider giving it a ⭐ on GitHub!

## 📄 License

This project is licensed under the **MIT License**.
