# توضیحات کد به زبان فارسی:
تابع count_words:

این تابع برای شمارش تعداد کلمات در یک متن استفاده می‌شود.
متن ورودی را به لیستی از کلمات تقسیم کرده و طول آن را برمی‌گرداند.
تابع count_text:

دو حالت را مدیریت می‌کند:
حالت WT (متن واردشده توسط کاربر): کاربر یک متن وارد می‌کند و تعداد کلمات آن محاسبه می‌شود.
حالت RM (متن فایل): کاربر نام فایل را وارد می‌کند، محتویات فایل خوانده شده و تعداد کلمات محاسبه می‌شود. اگر فایل پیدا نشود، پیام خطا نمایش داده شده و دوباره از کاربر درخواست فایل می‌شود.
تابع main:

نقطه شروع برنامه است. از کاربر می‌پرسد که آیا می‌خواهد متن را مستقیماً وارد کند یا از فایل استفاده کند.
اگر ورودی نامعتبر باشد، پیام خطا نمایش داده می‌شود.
امکان ادامه یا خروج از برنامه در پایان هر عملیات فراهم است.
اجرای برنامه (__name__ == "__main__"):

اگر فایل به صورت مستقیم اجرا شود، تابع main فراخوانی می‌شود. این ساختار تضمین می‌کند که برنامه به صورت ماژول استفاده شود.

# Code Explanation in English:
Function count_words:

This function counts the number of words in a given text.
It splits the input text into a list of words and returns the length of the list.
Function count_text:

Manages two cases:
Case WT (User-provided text): The user enters a text, and the number of words is calculated.
Case RM (File text): The user enters the name of a file, the file contents are read, and the number of words is calculated. If the file is not found, an error message is displayed, and the user is prompted again.
Function main:

The starting point of the program. It asks the user whether they want to enter text directly or use a file.
If the input is invalid, an error message is shown.
The user can choose to continue or exit the program after each operation.
Program Execution (__name__ == "__main__"):

# Kod Açıklamaları Türkçe:
count_words Fonksiyonu:

Bu fonksiyon, verilen bir metindeki kelime sayısını hesaplar.
Girdi metnini kelimelere böler ve listenin uzunluğunu döndürür.
count_text Fonksiyonu:

İki durumu yönetir:
WT Durumu (Kullanıcı tarafından girilen metin): Kullanıcı bir metin girer ve kelime sayısı hesaplanır.
RM Durumu (Dosya metni): Kullanıcı bir dosya adı girer, dosya içeriği okunur ve kelime sayısı hesaplanır. Eğer dosya bulunamazsa, hata mesajı gösterilir ve tekrar giriş istenir.
main Fonksiyonu:

Programın başlangıç noktasıdır. Kullanıcıya doğrudan metin mi yoksa dosya mı kullanmak istediği sorulur.
Geçersiz bir giriş yapılırsa, hata mesajı gösterilir.
Her işlemden sonra kullanıcı programı devam ettirme veya çıkış yapma seçeneğine sahiptir.
Programın Çalıştırılması (__name__ == "__main__"):

Eğer dosya doğrudan çalıştırılırsa, main fonksiyonu çağrılır. Bu yapı, programın modül olarak kullanılması durumunda istem dışı çalıştırılmasını engeller.

If the file is run directly, the main function is invoked. This ensures the program does not execute unintentionally if used as a module.
