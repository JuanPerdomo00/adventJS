def decode_filename(filename: str) -> str:
    return ".".join(filename.lstrip("0123456789_").split(".")[:2])


if __name__ == "__main__":
    print(decode_filename("2023122512345678_sleighDesign.png.grinchwa"))
    print(decode_filename("42_chimney_dimensions.pdf.hack2023"))
    print(decode_filename("987654321_elf-roster.csv.tempfile"))
