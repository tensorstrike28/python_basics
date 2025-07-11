def analyse_log(filename):
    with open(filename) as f:
        in_string = f.read().split('\n')
    status_dict = {}
    for line in in_string:
        name, status = line.split()
        if name in status_dict:
            status_dict[name].append(int(status))
        else:
            status_dict[name] = [int(status)]
    print(status_dict)


analyse_log('status.log')
