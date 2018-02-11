import argparse

output_file_valid_ips_name = 'validIPs.txt'
output_file_invalid_ips_name = 'invalidIPs.txt'

"""
IPv4 (32-bit) and IPv6 (64-bit)
IPv4 example 12:34:56:78
IPv6 example 1234:5678:9abc:def0:1234:5678:9abc:def0. 
Double colons (::) represent a string of zero entries so 1234:0:9abc:0:0:0:0:def0 could be 1234:0:9abc::def0
"""

def validate_ip_address(ip):
    """
    A function which checks if an IP address is valid
    returns: Boolean
    """
    if not ip:
        return False
    ip_components = ip.split('.')
    if len(ip_components) != 4:
        return False
    try:
        for part in ip_components:
            if 0 > int(part) > 255:
                # not a valid ip4 range
                return False
        return True
    except ValueError:
        # a component is empty or not an int
        return False
    

if __name__ == '__main__':
    # read the args and run the validation
    output_file_invalid_ips = open(output_file_invalid_ips_name, "w+")
    output_file_valid_ips = open(output_file_valid_ips_name, "w+")
    parser = argparse.ArgumentParser(description='Process a list of IP addresses')
    parser.add_argument('input', type=str,
                        help='An input file containing a list of IP addresses')
    args = vars(parser.parse_args())

    input_name = args.get('input')
    input_file = open(input_name, 'r')
    
    if input_file:
        line = input_file.readline()
        while line:
            # validate each IP
            line = input_file.readline()
            if (validate_ip_address(ip=line)):
                output_file_valid_ips.write(line)
            else:
                output_file_invalid_ips.write(line)
