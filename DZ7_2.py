def print_operation_table(operation, num_rows: int = 6, num_columns: int = 6) -> None:
    for y in range(1, num_rows+1):
        print(*([operation(x, y) for x in range(1, num_columns + 1)]), sep='\t')


def main() -> None:
    operations = [
        ('Умножение', lambda x, y: x * y),
        ('Сложение', lambda x, y: x + y),
        ('Вычитание', lambda x, y: x - y),
        ('Степень', lambda x, y: x**y)
    ]
    for operation_name, operation_function in operations:
        print(operation_name)
        print_operation_table(operation_function)
        print()


if __name__ == '__main__':
    main()