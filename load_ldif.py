from ldap3 import Server, Connection, ALL, LDIF
import os

# === Configuration ===
LDAP_SERVER = 'ldap://localhost'         # e.g., 'ldap://127.0.0.1'
LDAP_PORT = 389
BIND_DN = 'cn=admin,dc=example,dc=com'   # Change to your bind DN
BIND_PASSWORD = 'adminpassword'          # Change to your password
LDIF_FILE_PATH = 'sample.ldif'           # Path to your LDIF file

# === Function to parse LDIF entries ===
def parse_ldif(file_path):
    entries = []
    with open(file_path, 'r') as f:
        parser = LDIF(f)
        for dn, entry in parser.parse():
            entries.append((dn, entry))
    return entries

# === Main function to import LDIF to LDAP ===
def import_ldif_to_ldap(ldif_path):
    server = Server(LDAP_SERVER, port=LDAP_PORT, get_info=ALL)
    conn = Connection(server, user=BIND_DN, password=BIND_PASSWORD, auto_bind=True)

    entries = parse_ldif(ldif_path)
    result_log = []

    for dn, entry in entries:
        # Check if entry already exists
        if conn.search(search_base=dn, search_filter='(objectClass=*)', search_scope='BASE'):
            result_log.append((dn, 'Skipped (already exists)'))
            continue

        # Attempt to add entry
        if conn.add(dn, attributes=entry):
            result_log.append((dn, 'Added'))
        else:
            result_log.append((dn, f"Failed: {conn.result['description']}"))

    conn.unbind()
    return result_log

# === Run the script ===
if __name__ == '__main__':
    if not os.path.isfile(LDIF_FILE_PATH):
        print(f"LDIF file not found: {LDIF_FILE_PATH}")
    else:
        results = import_ldif_to_ldap(LDIF_FILE_PATH)
        for dn, status in results:
            print(f"{dn} -> {status}")
