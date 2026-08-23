import re
import unicodedata

def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return "-".join(re.findall(r"[a-z0-9]+", normalized.lower()))

if __name__ == "__main__":
    print(slugify("Golden URLs: A Practical Guide!"))
