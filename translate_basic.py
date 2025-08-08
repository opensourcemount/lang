#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Basic Ukrainian translation script for OPNsense
Translates the most common interface elements
"""

import re
import sys

# Dictionary of basic translations
translations = {
    # Basic actions
    "Add": "Додати",
    "Apply": "Застосувати", 
    "Save": "Зберегти",
    "Cancel": "Скасувати",
    "Delete": "Видалити",
    "Edit": "Редагувати",
    "Enable": "Увімкнути",
    "Disable": "Вимкнути",
    "Remove": "Видалити",
    "Update": "Оновити",
    "Refresh": "Оновити",
    "Reset": "Скинути",
    "Clear": "Очистити",
    "Close": "Закрити",
    "Open": "Відкрити",
    "Start": "Запустити",
    "Stop": "Зупинити",
    "Restart": "Перезапустити",
    "Reload": "Перезавантажити",
    "Submit": "Надіслати",
    "Search": "Пошук",
    "Filter": "Фільтр",
    "Sort": "Сортувати",
    "View": "Переглянути",
    "Show": "Показати",
    "Hide": "Приховати",
    "Import": "Імпортувати",
    "Export": "Експортувати",
    "Download": "Завантажити",
    "Upload": "Вивантажити",
    "Copy": "Копіювати",
    "Move": "Перемістити",
    "Backup": "Резервна копія",
    "Restore": "Відновити",
    
    # Status
    "Active": "Активний",
    "Inactive": "Неактивний",
    "Enabled": "Увімкнено",
    "Disabled": "Вимкнено",
    "Online": "В мережі",
    "Offline": "Не в мережі",
    "Connected": "Підключено",
    "Disconnected": "Відключено",
    "Running": "Працює",
    "Stopped": "Зупинено",
    "Failed": "Помилка",
    "Success": "Успішно",
    "Error": "Помилка",
    "Warning": "Попередження",
    "Information": "Інформація",
    "Status": "Статус",
    "State": "Стан",
    
    # Common words
    "Name": "Назва",
    "Description": "Опис",
    "Type": "Тип",
    "Value": "Значення",
    "Address": "Адреса",
    "Port": "Порт",
    "Protocol": "Протокол",
    "Interface": "Інтерфейс",
    "Network": "Мережа",
    "Gateway": "Шлюз",
    "Route": "Маршрут",
    "Rule": "Правило",
    "Policy": "Політика",
    "Service": "Служба",
    "User": "Користувач",
    "Group": "Група",
    "Password": "Пароль",
    "Username": "Ім'я користувача",
    "Email": "Електронна пошта",
    "Date": "Дата",
    "Time": "Час",
    "Size": "Розмір",
    "Version": "Версія",
    "License": "Ліцензія",
    "Configuration": "Конфігурація",
    "Settings": "Налаштування",
    "Options": "Параметри",
    "Properties": "Властивості",
    "Attributes": "Атрибути",
    "Parameters": "Параметри",
    "General": "Загальні",
    "Advanced": "Розширені",
    "Security": "Безпека",
    "System": "Система",
    "Network": "Мережа",
    "Firewall": "Брандмауер",
    "VPN": "VPN",
    "Services": "Служби",
    "Diagnostics": "Діагностика",
    "Logs": "Журнали",
    "Reports": "Звіти",
    "Statistics": "Статистика",
    "Monitoring": "Моніторинг",
    "Dashboard": "Панель керування",
    "Help": "Допомога",
    "About": "Про програму",
    
    # Yes/No
    "Yes": "Так",
    "No": "Ні",
    "OK": "Гаразд",
    "Confirm": "Підтвердити",
    "Continue": "Продовжити",
    "Abort": "Перервати",
    
    # Time units
    "Second": "Секунда",
    "Minute": "Хвилина", 
    "Hour": "Година",
    "Day": "День",
    "Week": "Тиждень",
    "Month": "Місяць",
    "Year": "Рік",
    
    # File operations
    "File": "Файл",
    "Folder": "Папка",
    "Directory": "Каталог",
    "Path": "Шлях",
    "Filename": "Ім'я файлу",
    
    # Network terms
    "IP": "IP",
    "IPv4": "IPv4",
    "IPv6": "IPv6",
    "MAC": "MAC",
    "DNS": "DNS",
    "DHCP": "DHCP",
    "HTTP": "HTTP",
    "HTTPS": "HTTPS",
    "FTP": "FTP",
    "SSH": "SSH",
    "TCP": "TCP",
    "UDP": "UDP",
    "ICMP": "ICMP",
    
    # Common phrases
    "Please wait": "Будь ласка, зачекайте",
    "Loading": "Завантаження",
    "Processing": "Обробка",
    "Complete": "Завершено",
    "Finished": "Закінчено",
    "Ready": "Готово",
    "Available": "Доступно",
    "Unavailable": "Недоступно",
    "Unknown": "Невідомо",
    "None": "Немає",
    "All": "Всі",
    "Any": "Будь-який",
    "Default": "За замовчуванням",
    "Custom": "Користувацький",
    "Auto": "Автоматично",
    "Manual": "Вручну",
    "Optional": "Необов'язково",
    "Required": "Обов'язково",
    "Valid": "Дійсний",
    "Invalid": "Недійсний",
    "Empty": "Порожньо",
    "Full": "Повний",
    "Partial": "Частковий",
    "Total": "Всього",
    "Count": "Кількість",
    "Number": "Номер",
    "ID": "Ідентифікатор",
    "Index": "Індекс",
    "Priority": "Пріоритет",
    "Weight": "Вага",
    "Level": "Рівень",
    "Mode": "Режим",
    "Method": "Метод",
    "Format": "Формат",
    "Content": "Вміст",
    "Data": "Дані",
    "Information": "Інформація",
    "Details": "Деталі",
    "Summary": "Підсумок",
    "Overview": "Огляд",
    "Preview": "Попередній перегляд",
    "Example": "Приклад",
    "Sample": "Зразок",
    "Template": "Шаблон",
    "Pattern": "Шаблон",
    "Match": "Збіг",
    "Result": "Результат",
    "Output": "Вивід",
    "Input": "Ввід",
    "Source": "Джерело",
    "Target": "Ціль",
    "Destination": "Призначення",
    "Origin": "Походження",
    "Location": "Розташування",
    "Position": "Позиція",
    "Range": "Діапазон",
    "Limit": "Обмеження",
    "Maximum": "Максимум",
    "Minimum": "Мінімум",
    "Average": "Середнє",
    "Current": "Поточний",
    "Previous": "Попередній",
    "Next": "Наступний",
    "First": "Перший",
    "Last": "Останній",
    "New": "Новий",
    "Old": "Старий",
    "Recent": "Останній",
    "Latest": "Найновіший",
    "Updated": "Оновлено",
    "Modified": "Змінено",
    "Created": "Створено",
    "Deleted": "Видалено",
    "Removed": "Видалено",
    "Added": "Додано",
    "Changed": "Змінено",
    "Saved": "Збережено",
    "Loaded": "Завантажено",
    "Installed": "Встановлено",
    "Uninstalled": "Видалено",
    "Configured": "Налаштовано",
    "Unconfigured": "Не налаштовано",
    "Activated": "Активовано",
    "Deactivated": "Деактивовано",
    "Locked": "Заблоковано",
    "Unlocked": "Розблоковано",
    "Protected": "Захищено",
    "Unprotected": "Незахищено",
    "Secure": "Безпечний",
    "Insecure": "Небезпечний",
    "Public": "Публічний",
    "Private": "Приватний",
    "Internal": "Внутрішній",
    "External": "Зовнішній",
    "Local": "Локальний",
    "Remote": "Віддалений",
    "Global": "Глобальний",
    "Regional": "Регіональний",
    "National": "Національний",
    "International": "Міжнародний"
}

def translate_po_file(filename):
    """Translate basic terms in PO file"""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count translations made
    translated_count = 0
    
    for english, ukrainian in translations.items():
        # Pattern to match exact msgid with the English term
        pattern = f'msgid "{re.escape(english)}"\nmsgstr ""'
        replacement = f'msgid "{english}"\nmsgstr "{ukrainian}"'
        
        if pattern in content:
            content = content.replace(pattern, replacement)
            translated_count += 1
            print(f"Translated: {english} -> {ukrainian}")
    
    # Write back the file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\nTotal translations made: {translated_count}")
    return translated_count

if __name__ == "__main__":
    filename = "uk_UA.po"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    
    print(f"Translating basic terms in {filename}...")
    translate_po_file(filename)
    print("Translation complete!")

