# Считывание пользовательских данных
# Программа должна запрашивать у пользователя следующую информацию:


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
vcc = 'il1Lo0O'
import time
import random

def _ask_int(prompt, default):
    while True:
        raw = input(f"{prompt} (по умолчанию {default}): ").strip()
        if raw == "":
            return default
        if raw.isdigit():
            return int(raw)
        print("Введите целое число.")

def _ask_yes_no(prompt, default): # опросник пользователя
    default_text = "Y" if default else "N"
    while True:
        raw = input(f"{prompt} (Y/N, по умолчанию {default_text}): ").strip()
        if raw == "":
            return default # защита от дурака. при нажатии на ентер выбирается дефолтное значение
        if raw.upper() == "Y":
            return True
        if raw.upper() == "N":
            return False
        print("Введите Y или N.")
def oprosnik():

    print('Привет, здесь можно создать свой безопасный пароль')
    time.sleep(1)
    print('Для создания паролей программа запросит у вас ответы на некоторые вопросы!')
    time.sleep(1)
    count_of_password = _ask_int('Для начала укажите количество паролей которые нужно сгенерировать', 5)
    len_of_password = _ask_int('Укажите Длину одного пароля', 10)
    flag_digits = _ask_yes_no('Включать ли цифры?', True)
    flag_big_letter = _ask_yes_no('Включать ли прописные буквы (большие)?', True)
    flag_small_letter = _ask_yes_no('Включать ли строчные буквы?', True)
    flag_special_character = _ask_yes_no('Включать ли специальные символы (!#$%&*+-=?@^_)?', True)
    flag_strange_simbols = _ask_yes_no('Убрать ли неоднозначные символы? (il1Lo0O)', True)
    flags = [count_of_password, len_of_password, flag_digits, flag_big_letter, flag_small_letter, flag_special_character, flag_strange_simbols]

    return flags
def build_chars(flags): # здесь я формирую строку с выбранными символами
    _, _, flag_digits, flag_big_letter, flag_small_letter, flag_special_character, flag_strange_simbols = flags
    chars = ''
    if flag_digits:
        chars += digits
    if flag_big_letter:
        chars += uppercase_letters
    if flag_small_letter:
        chars += lowercase_letters
    if flag_special_character:
        chars += punctuation
    if flag_strange_simbols:
        # remove ambiguous symbols
        chars = ''.join(c for c in chars if c not in vcc)
    return chars

def create_password(count_of_password, len_of_password, chars):
    passwords = []
    for _ in range(count_of_password):
        password = ''.join(random.choice(chars) for _ in range(len_of_password))
        passwords.append(password)
    return passwords

if __name__ == '__main__':
    flags = oprosnik()
    chars = build_chars(flags)
    if chars == "":
        print("Нельзя сгенерировать пароль: выбран пустой набор символов.")
        raise SystemExit(1)
    count_of_password, len_of_password = flags[0], flags[1]
    passwords = create_password(count_of_password, len_of_password, chars)
    print("Ваши пароли:")
    for i, p in enumerate(passwords, start=1):
        print(f"{i}. {p}")
    input("Нажмите Enter для выхода...")