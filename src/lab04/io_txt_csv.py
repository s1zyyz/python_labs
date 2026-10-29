import csv
from pathlib import *


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Открывает файл целиком и возвращает весь текст одной строкой.

    Если нужна другая кодировка, укажи её так: encoding="cp1251".
    Ошибки (если файла нет или кодировка не подошла) не ловим — пусть падают.
    """
    return Path(path).read_text(encoding=encoding)


def write_csv(rows: list[tuple | list], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    """Записывает табличку в CSV-файл через запятую.

    Если передан заголовок (header), он встает на самую первую строчку.
    Если в таблице строки разной длины — программа выдает ошибку ValueError.
    """
    rows = list(rows)
    if len({len(r) for r in rows}) > 1:
        raise ValueError("Строки в rows имеют разную длину")

    with Path(path).open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        w.writerows(rows)
