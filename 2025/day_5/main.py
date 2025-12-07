from datetime import datetime, timezone
import math


def time_until_take_off(from_time: str, take_off_time: str) -> int:
    run = datetime.strptime(take_off_time.replace(
        "*", "-").replace("@", " ").replace("|", ":")[:-3], "%Y-%m-%d %H:%M:%S")
    now = datetime.strptime(from_time.replace(
        "*", "-").replace("@", " ").replace("|", ":")[:-3], "%Y-%m-%d %H:%M:%S")

    return math.floor((run - now).total_seconds())


if __name__ == "__main__":
    takeoff = "2025*12*25@00|00|00 NP"

    print(time_until_take_off("2025*12*24@23|59|30 NP", takeoff))
    print(time_until_take_off("2025*12*25@00|00|00 NP", takeoff))
    print(time_until_take_off("2025*12*25@00|00|12 NP", takeoff))
