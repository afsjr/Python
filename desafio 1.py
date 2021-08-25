def open_file(name):
    try:
        f = open(name, "r")
        return f
    except FileNotFoundError as e:
        print("During the opening an error was found: ", e)
        exit()

def create_file(name):
    f = open(name, "w")
    return f


def read_file(file):
    file_content = file.readlines()
    return file_content


def find_total_months(file):
    total_months = len(file_content[1:])
    return total_months


def find_values(file_content):
    values = []
    for data in file_content[1:]:
        values.append(data[9:-1])
    return values


def find_months(file_content):
    months = []
    for data in file_content[1:]:
        months.append(data[0:8])
    return months


def find_total(values):
    soma = 0
    for num in values:
        soma += int(num)
    return soma


def find_mean(soma, total_months):
    mean = soma / total_months
    return mean


def find_difference(values):
    difference = []
    for v in range(len(values) - 1):
        difference.append(int(values[v + 1]) - int(values[v]))
    return difference


if __name__ == "__main__":
    user_file = 'dados_financeiro.txt'

    file = open_file(user_file)
    read_file(file)
    file.close()
    find_total_months(file_content)
    find_values(file_content)
    total = find_total(values)
    mean = find_mean(soma, total_months)
    find_months(file_content)
    difference = find_difference(values)
    difference_mean = sum(difference) / len(difference)

    high_num = max(difference)
    lowest_num = min(difference)

    high_month = months[(difference.index(high_num)) + 1]
    lowest_month = months[(difference.index(lowest_num)) + 1]

    relatorio = create_file("relatorio.txt")
    relatorio.write(" Analise financeira" + "\n" +
                    "----------------------------" + "\n")
    relatorio.write(f"Total de meses: {total_months}")
    relatorio.write(f"\nTotal: $ {total}")
    relatorio.write(f"\nMédia: $ {mean:.2f}")
    relatorio.write(f"\nVariação da média: $ {difference_mean:.2f}")
    relatorio.write(f"\nMaior aumento nos lucros: {high_month} ($ {high_num})")
    relatorio.write(f"\nMaior redução nos lucros: {lowest_month} ($ {lowest_num})")
    relatorio.close()