def format_record(rec: tuple[str, str, float]) -> str:
    
    if not isinstance(rec, tuple) or len(rec) != 3:
        raise TypeError

    fio, group, gpa = rec

    if not isinstance(fio, str):
        raise TypeError
    if not isinstance(group, str):
        raise TypeError
    if not isinstance(gpa, (int, float)):
        raise TypeError
    
    parts = fio.split()
    if len(parts) < 2:
        raise ValueError

    last_name = parts[0].capitalize()
    initials = "".join(p[0].upper() + "." for p in parts[1:3])

    
    group = " ".join(group.split())
    if not group:
        raise ValueError("группа не может быть пустой")

   
    if not (0.0 <= gpa <= 5.0):
        raise ValueError("GPA должен быть в диапазоне [0.0, 5.0]")

    return f"{last_name} {initials}, гр. {group}, GPA {gpa:.2f}"

""" print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999))) """
