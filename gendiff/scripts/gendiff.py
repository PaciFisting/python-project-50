import argparse
import json


def generate_diff(first_dict, second_dict):
    diff_dict = {}
    for key in first_dict:
        if key not in second_dict:
            diff_dict[f'  - {key}'] = first_dict[key]
        else:
            if first_dict[key] == second_dict[key]:
                diff_dict[f'    {key}'] = first_dict[key]
            else:
                diff_dict[f'  - {key}'] = first_dict[key]
                diff_dict[f'  + {key}'] = second_dict[key]
    for key in second_dict:
        if key not in first_dict:
            diff_dict[f'  + {key}'] = second_dict[key]
    sorted_diff = dict(
        sorted(diff_dict.items(), key=lambda x: x[0].lstrip('+- '))
        )
    return sorted_diff


def make_diff():
    parser = argparse.ArgumentParser(
        description='Compares two JSON files and shows the difference.'
        )
    parser.add_argument(
        'first_file', type=str, help='Path to the first JSON file'
        )
    parser.add_argument(
        'second_file', type=str, help='Path to the second JSON file'
        )
    args = parser.parse_args(['file1.json', 'file2.json'])

    first_dict = json.load(open(args.first_file))
    second_dict = json.load(open(args.second_file))

    diff = generate_diff(first_dict, second_dict)
    result = ['{']
    for key, value in diff.items():
        result.append(f'  {key}: {value}')
    result.append('}')
    return '\n'.join(result)


def main():
    return make_diff()


if __name__ == "__main__":    
    main()