from datetime import datetime, timedelta, timezone

def filetime_to_datetime(filetime: str):
    filetime_int = int(filetime, 16)

    total_seconds = filetime_int // 10000000
    remainder_100ns = filetime_int % 10000000

    utc = datetime.utcfromtimestamp(total_seconds - 11644473600)
    utc = utc.replace(tzinfo=timezone.utc)

    kst = utc.astimezone(timezone(timedelta(hours=9)))

    fractional_100ns = remainder_100ns * 100
    fractional_str = f"{fractional_100ns:07d}"[:7]

    iso_kst = kst.strftime("%Y-%m-%dT%H:%M:%S") + f".{fractional_str}+09:00"
    iso_utc = utc.strftime("%Y-%m-%dT%H:%M:%S") + f".{fractional_str}+00:00"

    return iso_utc, iso_kst

utc, kst = filetime_to_datetime('0x01DB686A7F6CA86E')

print("KST", kst)
print("UTC", utc)
