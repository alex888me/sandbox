from M2Crypto import Engine, m2

engine_id = "pkcs11"  # The usual identifier for the OpenSSL PKCS#11 engine.
dynamic_path = "/path/to/your/dynamic/engine.so"  # This path might vary based on your installation.

# Load the dynamic engine.
Engine.load_dynamic_engine(engine_id, dynamic_path)
engine = Engine.Engine_by_id(engine_id)

# Engine-specific initialization.
if not engine.init():
    raise Exception("Engine initialization failed.")

from M2Crypto import SSL

ctx = SSL.Context()
ctx.set_info_callback()

# Set engine-based private key and certificate
if not ctx.load_client_ca("path_to_your_cert.pem"):
    raise Exception("Failed to load client CA certificate.")
if not ctx.set_default_verify_paths():
    raise Exception("Failed to set default verify paths.")

# Set engine and private key for the SSL context
ctx.set_engine(engine)
user_key = engine.load_private_key("pkcs11:your_configuration_string_here", callback=None)
ctx.use_privatekey(user_key)

import requests

# Convert M2Crypto context to standard Python SSL context
stdlib_context = SSL.Context._get_stdlib_context(ctx)

response = requests.get("https://your.target.url", verify=True, cert=('path_to_your_cert.pem', None), proxies={"https": "https://localhost:8080"}, headers=headers, data=data)

print(response.text)
