def draw_table(data: list[dict[str, str | int]]) -> str:
    # Code here
    table = ""
    column_names = list(data[0].keys())
    column_sizes = {col: len(col) for col in column_names}

    for row in data:
        for col in column_names:
            column_sizes[col] = max(column_sizes[col], len(str(row[col])))

    row_separator = (
        "+" + "+".join("-" * (size + 2) for size in column_sizes.values()) + "+"
    )

    header = "|"
    for col in column_names:
        formatted_col = col[0].upper() + col[1:]
        header += f" {formatted_col.ljust(column_sizes[col])} |"

    table += f"{row_separator}\n{header}\n{row_separator}\n"

    for row in data:
        table += "|"
        for col in column_names:
            value = str(row[col])
            table += f" {value.ljust(column_sizes[col])} |"
        table += "\n"

    table += row_separator
    return table


if __name__ == "__main__":
    print(
        draw_table(
            [
                {"name": "Alice", "city": "London"},
                {"name": "Bob", "city": "Paris"},
                {"name": "Charlie", "city": "New York"},
            ]
        )
    )
