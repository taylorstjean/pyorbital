from datetime import datetime

dt = 5e2  # (s)


def day_num():

    DT = datetime.utcnow()

    y = DT.year
    m = DT.month
    D = DT.day

    decimal_hour = ((DT.hour * 3600.0) + (DT.minute * 60.0) + DT.second) / 3600.0

    d = (367 * y) - (7 * (y + (m + 9) // 12) // 4) - (3 * ((y + (m - 9) // 7) / 100 + 1) // 4) + (
                275 * m // 9) + D - 730515

    return int(d) + (decimal_hour / 24.0)
