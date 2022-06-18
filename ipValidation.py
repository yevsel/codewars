def ip_validation(ip_string):
    splited = ip_string.split('.')
    condition = True
    if len(splited) == 4:
        for i in range(len(splited)):
            if splited[i][0] != '0' and int(splited[i]) > 0 and int(splited[i]) <= 255:
                return True
            return False
    else:
        return False
