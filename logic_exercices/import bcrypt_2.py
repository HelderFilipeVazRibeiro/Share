import bcrypt

# Define the password
senha = '12345'

# Generate a salt with a cost factor of 8
salt = bcrypt.gensalt(8)

# Print the generated salt
print(salt)

# Hash the password using the generated salt
hash = bcrypt.hashpw(senha.encode('utf-8'), salt)

# Print the generated hash
print(f"Hash = {hash}")
