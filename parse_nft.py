def parse_nft_script(file_path):
    with open(file_path, 'r') as file:
        script = file.read()

    # Regex to find port redirection rules, assuming the format is 'tcp dport {from_port} redirect to :{to_port}'
    pattern = re.compile(r'tcp dport (\d+) redirect to :(\d+)')

    port_redirects = []
    matches = pattern.finditer(script)
    for match in matches:
        from_port, to_port = match.groups()
        # You can modify the 'name' parameter as needed
        port_redirect = PortRedirect('LDAP', from_port, to_port)
        port_redirects.append(port_redirect)

    return port_redirects