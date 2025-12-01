import re


def find_in_agenda(agenda: str, phone: str) -> dict | None:
    # Code here
    lines = agenda.split("\n")
    for line in lines:
        # Encuentra todos los números de teléfono (sin incluir el '+')
        phones = re.findall(r"\+?([0-9-]+)", line)
        if phone in phones:
            # Busca el nombre dentro de < >
            name_match = re.search(r"<(.*?)>", line)
            name = name_match.group(1).strip() if name_match else None

            # Busca direcciones flexibles (texto seguido de un número o solo texto)
            address_match = re.search(r"([A-Za-zÀ-ÿ\s]+(?:\d{1,3})?)", line)
            address = address_match.group(0).strip() if address_match else None

            # Filtrar resultados no válidos
            if name and address:
                return {"name": name, "address": address}
    return None


if __name__ == "__main__":
    agenda = """+34-600-123-456 Calle Gran Via 12 <Juan Perez>
Plaza Mayor 45 Madrid 28013 <Maria Gomez> +34-600-987-654
<Carlos Ruiz> +1-800-555-0199 Fifth Ave New York"""
    print(
        find_in_agenda(agenda, "34-600-123-456")
    )  # { "name": "Juan Perez", "address": "Calle Gran Via 12" }
    print(
        find_in_agenda(agenda, "800-555-0199")
    )  # { "name": "Carlos Ruiz", "address": "Fifth Ave New York" }

    print(find_in_agenda(agenda, "123-456"))  # None
