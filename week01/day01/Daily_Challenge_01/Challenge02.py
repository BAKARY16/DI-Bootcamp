from datetime import datetime, date


def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def calculate_age(birth: date, today: date = date.today()) -> int:
    age = today.year - birth.year
    if (today.month, today.day) < (birth.month, birth.day):
        age -= 1
    return age


def render_cake(candles: int) -> str:
    candles_str = 'i' * candles
    top = f"       ___{candles_str}___"
    lines = [
        top,
        "      |:H:a:p:p:y:|",
        "    __|___________|__",
        "   |^^^^^^^^^^^^^^^^^|",
        "   |:B:i:r:t:h:d:a:y:|",
        "   |                 |",
        "   ~~~~~~~~~~~~~~~~~~~",
    ]
    return "\n".join(lines)


def main() -> None:
    s = input("Entrez votre date de naissance (DD/MM/YYYY) : ").strip()
    try:
        bd = datetime.strptime(s, "%d/%m/%Y").date()
    except Exception:
        print("Format invalide. Utilisez DD/MM/YYYY, par ex. 31/12/1990")
        return

    today = date.today()
    age = calculate_age(bd, today)
    if age < 0:
        print("Date de naissance dans le futur. Vérifiez votre saisie.")
        return

    candles = age % 10
    leap = is_leap_year(bd.year)

    info = f"Vous avez {age} ans (né(e) le {bd.strftime('%d/%m/%Y')})."
    info += f" Nombre de bougies = {candles}."
    info += " Année de naissance bissextile." if leap else " Année de naissance non bissextile."
    print(info)

    # Afficher un ou deux gâteaux
    count = 2 if leap else 1
    for i in range(count):
        print('\n' + render_cake(candles) + '\n')


if __name__ == "__main__":
    main()

