import pwd

def get_home_directory(username):
    try:
        user_info = pwd.getpwnam(username)
        return user_info.pw_dir
    except KeyError:
        return None

# Example usage:
username = 'some_user'
home_directory = get_home_directory(username)

if home_directory:
    print(f"The home directory for {username} is: {home_directory}")
else:
    print(f"No user with the name {username} was found.")