import sqlite3
import hashlib
from googletrans import Translator

LANGUAGES = {
    "af": "Африкаанс",
    "sq": "Албанский",
    "am": "Амхарский",
    "ar": "Арабский",
    "hy": "Армянский",
    "az": "Азербайджанский",
    "eu": "Баскский",
    "be": "Белорусский",
    "bn": "Бенгальский",
    "bs": "Боснийский",
    "bg": "Болгарский",
    "ca": "Каталанский",
    "ceb": "Себуанский",
    "ny": "Чичева",
    "zh-cn": "Китайский (упрощенный)",
    "zh-tw": "Китайский (традиционный)",
    "co": "Корсиканский",
    "hr": "Хорватский",
    "cs": "Чешский",
    "da": "Датский",
    "nl": "Голландский",
    "en": "Английский",
    "eo": "Эсперанто",
    "et": "Эстонский",
    "tl": "Тагальский",
    "fi": "Финский",
    "fr": "Французский",
    "fy": "Фризский",
    "gl": "Галисийский",
    "ka": "Грузинский",
    "de": "Немецкий",
    "el": "Греческий",
    "gu": "Гуджарати",
    "ht": "Гаитянский креольский",
    "ha": "Хауса",
    "haw": "Гавайский",
    "iw": "Иврит",
    "he": "Иврит",
    "hi": "Хинди",
    "hmn": "Хмонг",
    "hu": "Венгерский",
    "is": "Исландский",
    "ig": "Игбо",
    "id": "Индонезийский",
    "ga": "Ирландский",
    "it": "Итальянский",
    "ja": "Японский",
    "jw": "Яванский",
    "kn": "Каннада",
    "kk": "Казахский",
    "km": "Кхмерский",
    "ko": "Корейский",
    "ku": "Курдский (курманджи)",
    "ky": "Киргизский",
    "lo": "Лаосский",
    "la": "Латинский",
    "lv": "Латышский",
    "lt": "Литовский",
    "lb": "Люксембургский",
    "mk": "Македонский",
    "mg": "Малагасийский",
    "ms": "Малайский",
    "ml": "Малаялам",
    "mt": "Мальтийский",
    "mi": "Маори",
    "mr": "Марати",
    "mn": "Монгольский",
    "my": "Бирманский",
    "ne": "Непальский",
    "no": "Норвежский",
    "or": "Одия",
    "ps": "Пушту",
    "fa": "Персидский",
    "pl": "Польский",
    "pt": "Португальский",
    "pa": "Пенджаби",
    "ro": "Румынский",
    "ru": "Русский",
    "sm": "Самоанский",
    "gd": "Шотландский гэльский",
    "sr": "Сербский",
    "st": "Сесото",
    "sn": "Шона",
    "sd": "Синдхи",
    "si": "Сингальский",
    "sk": "Словацкий",
    "sl": "Словенский",
    "so": "Сомали",
    "es": "Испанский",
    "su": "Суданский",
    "sw": "Суахили",
    "sv": "Шведский",
    "tg": "Таджикский",
    "ta": "Тамильский",
    "te": "Телугу",
    "th": "Тайский",
    "tr": "Турецкий",
    "uk": "Украинский",
    "ur": "Урду",
    "ug": "Уйгурский",
    "uz": "Узбекский",
    "vi": "Вьетнамский",
    "cy": "Валлийский",
    "xh": "Кхоса",
    "yi": "Идиш",
    "yo": "Йоруба",
    "zu": "Зулу",
}


def log_in(password) -> str:
    pw_hash = hashlib.new("sha512")
    pw_hash.update(password.encode())
    pw_hex = pw_hash.hexdigest()
    return pw_hex


def get_connection():
    try:
        con = sqlite3.connect("./database.db")
        return con
    except Exception as e:
        print(e)
        raise e


def create_table(
    stmt: str,
):
    con = get_connection()
    cursor = con.cursor()
    cursor.execute(stmt)
    con.commit()
    cursor.close()
    con.close()


def add(stmt: str, values: tuple = ()):
    con = get_connection()
    cursor = con.cursor()
    cursor.execute(stmt, values)
    con.commit()
    cursor.close()
    con.close()


def select(
    stmt: str,
    values: tuple = (),
):
    con = get_connection()
    cursor = con.cursor()
    res = None
    cursor.execute(stmt, values)
    res = cursor.fetchall()
    con.commit()
    cursor.close()
    con.close()
    return res


def translate(text: str, default_language: str, language_to_translate: str):
    translator = Translator()
    translated_text = translator.translate(
        text, src=default_language, dest=language_to_translate
    )
    print(f"Перевод: {translated_text.text}")


def table_exists(table_name):
    con = get_connection()
    cursor = con.cursor()
    stmt = "SELECT name FROM sqlite_master WHERE type='table' AND name=?"
    cursor.execute(stmt, (table_name,))
    result = cursor.fetchone()
    con.commit()
    cursor.close()
    con.close()
    if result:
        return True
    else:
        return False
