from netifaces import interfaces, ifaddresses, AF_INET


def get_local_ip():
    for ifaceName in interfaces():
        for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] ):
            if not i['addr'] == 'No IP addr' and not i['addr'] == '127.0.0.1':
                return i['addr']

