import csv
from pathlib import Path
from typing import Iterable, Sequence


def ensure_parent_dir(path: str | Path):
    """
    Создаёт родительские директории для указанного файла, если их ещё нет.
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Открывает текстовый файл в указанной кодировке и возвращает его содержимое
    как одну строку.

    По умолчанию используется кодировка UTF-8. Если входной файл сохранён
    в другой кодировке , передайте её через аргумент
    encoding:
        text = read_text("data/lab04/input.txt", encoding="cp1251")

        FileNotFoundError: если файл по указанному пути не найден.
        UnicodeDecodeError: если байты файла не удаётся декодировать
            в указанной кодировке.
    """
    p = Path(path)
    return p.read_text(encoding=encoding)


def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    """
    перезаписывает CSV-файл с разделителем ','.

    Перед записью проверяет, что все строки в rows имеют одинаковую длину
    (и совпадают с длиной header, если он передан), а также автоматически
    создаёт родительские директории.

        ValueError: если строки в rows имеют разную длину или не совпадают
            по длине с заголовком header.
    """
    p = Path(path)

    
    rows_list = [list(row) for row in rows]

   
    if rows_list:
        expected_len = len(rows_list[0])
        for index, row in enumerate(rows_list):
            if len(row) != expected_len:
                raise ValueError("Все строки CSV должны иметь одинаковую длину.")
        if header is not None and len(header) != expected_len:
            raise ValueError("Длина заголовка не совпадает с длиной строк.")

   
    ensure_parent_dir(p)

  
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)


