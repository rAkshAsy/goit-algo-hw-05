import re
import sys
from pathlib import Path



def load_logs(file_path: str) -> list:
    try:
        with open(file_path, 'r', encoding='UTF-8') as log_file:
            logs_list = [line.strip() for line in log_file]
            return logs_list
    except FileExistsError:
        print("FileExistsError")
    except FileNotFoundError:
        print("FileNotFoundError")


def parse_log_line(line: str) -> dict:
    line_list = line.split()
    first_word_msg = line_list[3]
    msg_pattern = first_word_msg + r'.+$'
    msg = re.search(msg_pattern, line)
    line_dict = {
        'date': line_list[0],
        'time': line_list[1],
        'level': line_list[2],
        'msg': msg.group()
    }
    return line_dict


def filter_logs_by_level(logs: list, level: str) -> list:
    filterung_list = [parse_log_line(line) for line in logs]
    filtred_logs = filter(lambda line: line['level'].casefold() == level.casefold(), filterung_list)
    return list(filtred_logs)

def count_logs_by_level(logs: list) -> dict:
    counter = {}
    for line in logs:
        line_dict = parse_log_line(line)
        if line_dict['level'] in counter:
            counter[line_dict['level']] += 1
        else:
            counter[line_dict['level']] = 1

    return counter


def display_log_counts(counts: dict):
    level_column = 'Рівень логування'
    count_column = 'Кiлькість'
    header = '{:<17}|{:>10}'.format(level_column, count_column)
    header_underline = '-'*17 + '|' + '-'*10
    print(header, header_underline, sep='\n')
    for key, value in counts.items():
        print(f'{key:<17}|{value:^10}')


def main():
    try:
        log_path = sys.argv[1]
    except IndexError:
        log_path = None

    try:
        filter_cmd = sys.argv[2]
    except IndexError:
        filter_cmd = None

    if log_path:
        logs = load_logs(log_path)
        if type(logs) == list:
                counted = count_logs_by_level(logs)
                display_log_counts(counted)
                if filter_cmd:
                    logs_by_level = filter_logs_by_level(logs, filter_cmd)
                    if logs_by_level:
                        print(f'Деталі логів для рівня \'{filter_cmd.upper()}\':')
                        for line in logs_by_level:
                            print(f'{line['date']} {line['time']} - {line['msg']}')
                    else:
                        print('Please, enter valid filter key.')
        else:
            print(f'Something wrong with file path. Сheck if the file path is entered correctly:\n{log_path}')
    else:
        print("There`s no path =)")


if __name__ == "__main__":
    main()