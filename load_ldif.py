from ldap3 import Server, Connection, ALL, SUBTREE
import os

# === Configuration ===
LDAP_SERVER = 'ldap://localhost'
LDAP_PORT = 389
BIND_DN = 'cn=admin,dc=example,dc=com'
BIND_PASSWORD = 'adminpassword'
BASE_DN = 'dc=example,dc=com'  # Root of the subtree to delete

# === Connect and Delete Function ===
def delete_subtree(base_dn):
    server = Server(LDAP_SERVER, port=LDAP_PORT, get_info=ALL)
    conn = Connection(server, user=BIND_DN, password=BIND_PASSWORD, auto_bind=True)

    # Search for all entries under base_dn
    conn.search(search_base=base_dn, search_filter='(objectClass=*)', search_scope=SUBTREE, attributes=['dn'])
    entries = [entry.entry_dn for entry in conn.entries]

    # Sort by DN depth, deepest first
    entries.sort(key=lambda dn: dn.count(','), reverse=True)

    result_log = []
    for dn in entries:
        if conn.delete(dn):
            result_log.append((dn, 'Deleted'))
        else:
            result_log.append((dn, f"Failed: {conn.result['description']}"))

    conn.unbind()
    return result_log

# === Run the script ===
if __name__ == '__main__':
    results = delete_subtree(BASE_DN)
    for dn, status in results:
        print(f"{dn} -> {status}")
