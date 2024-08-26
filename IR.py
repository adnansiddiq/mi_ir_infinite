import glob
import os
import json


def print_all_ir_files(directory_path):
    file_pattern = f"{directory_path}/*.ir"
    ir_files = glob.glob(file_pattern)

    output_folder = os.path.join(os.getcwd(), 'Codes')
    os.makedirs(output_folder, exist_ok=True)

    for file_path in ir_files:
        with open(file_path, 'r') as file:
            file_name = os.path.splitext(os.path.basename(file_path))[0]
            print(file_name)


def read_files_with_ir_extension(directory_path):
    file_pattern = f"{directory_path}/*.ir"
    ir_files = glob.glob(file_pattern)

    output_folder = os.path.join(os.getcwd(), 'Codes')
    os.makedirs(output_folder, exist_ok=True)

    for file_path in ir_files:
        with open(file_path, 'r') as file:
            content = file.read()
            file_name = os.path.splitext(os.path.basename(file_path))[0]
            output_file_path = os.path.join(output_folder, f"{file_name}.json")

            with open(output_file_path, 'w') as json_file:
                data = dict()
                signals = []
                current_signal = None
                lines = content.split('\n')
                key, value = lines[0].split(':')
                data[key] = value
                key, value = lines[1].split(':')
                data[key] = value
                key, value = lines[2].lstrip('#').split(';')[0].split(':')
                data[key] = value
                try:
                    key, value = lines[2].split(';')[1].split(':')
                    data[key] = value
                except:
                    _, key, value = lines[2].split(';')[1].split(':')
                    data[key] = value
                try:
                    key, value = lines[2].split(';')[2].split(':')
                    data[key] = value
                except:
                    pass

                for i in range(4, len(lines)-1):
                    if lines[i].startswith('#'):
                        if current_signal:
                            signals.append(current_signal)
                        current_signal = dict()
                    else:
                        try:
                            key, *value = lines[i].split(':')
                            current_signal[key] = ':'.join(value)
                        except:
                            pass
                signals.append(current_signal)
                data['Signals'] =signals
                print(file_name)
                json.dump(data, json_file, indent=2)


def read_file_with_ir_extension(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        data = dict()
        signals = []
        current_signal = None
        lines = content.split('\n')
        key, value = lines[0].split(':')
        data[key] = value
        key, value = lines[1].split(':')
        data[key] = value
        key, value = lines[2].lstrip('#').split(';')[0].split(':')
        data[key] = value
        try:
            key, value = lines[2].split(';')[1].split(':')
            data[key] = value
        except:
            _, key, value = lines[2].split(';')[1].split(':')
            data[key] = value
        try:
            key, value = lines[2].split(';')[2].split(':')
            data[key] = value
        except:
            pass

        for i in range(4, len(lines) - 1):
            if lines[i].startswith('#'):
                if current_signal:
                    signals.append(current_signal)
                current_signal = dict()
            else:
                try:
                    key, *value = lines[i].split(':')
                    current_signal[key] = ':'.join(value)
                except:
                    pass
        signals.append(current_signal)
        data['Signals'] = signals
        return data


def get_ir(file_name):
    output_folder = os.path.join(os.getcwd(), 'Codes')
    os.makedirs(output_folder, exist_ok=True)

    with open(f'{file_name}.ir', 'r') as file:
        content = file.read()
        output_file_path = os.path.join(output_folder, f"{file_name}.json")
        data = dict()
        signals = []
        current_signal = None
        lines = content.split('\n')
        key, value = lines[0].split(':')
        data[key] = value
        key, value = lines[1].split(':')
        data[key] = value
        key, value = lines[2].lstrip('#').split(';')[0].split(':')
        data[key] = value
        try:
            key, value = lines[2].split(';')[1].split(':')
            data[key] = value
        except:
            _, key, value = lines[2].split(';')[1].split(':')
            data[key] = value
        try:
            key, value = lines[2].split(';')[2].split(':')
            data[key] = value
        except:
            pass

        for i in range(4, len(lines) - 1):
            if lines[i].startswith('#'):
                if current_signal:
                    signals.append(current_signal)
                current_signal = dict()
            else:
                try:
                    key, *value = lines[i].split(':')
                    current_signal[key] = ':'.join(value)
                except:
                    pass
        signals.append(current_signal)
        data['Signals'] = signals
        return data


def delete_files_with_extension(directory, extension):
    # Construct the pattern to match files with the specified extension
    pattern = os.path.join(directory, f"*.{extension}")

    # Use glob to get a list of file paths matching the pattern
    file_list = glob.glob(pattern)

    # Delete each file
    for file_path in file_list:
        try:
            os.remove(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

