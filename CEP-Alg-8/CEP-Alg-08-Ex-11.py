def codificar_run_length(s):
    if s == "":
        return []

    char = s[0]
    count = 1

    while count < len(s) and s[count] == char:
        count += 1

    return [char, count] + codificar_run_length(s[count:])