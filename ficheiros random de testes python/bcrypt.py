import bcrypt

# Define the password
senha = '12345'


# Generate a salt with a cost factor of 8
salt = bcrypt.gensalt(8)

# Print the generated salt
print(salt)
# $2a$08$K02Yy9Sn2mDReCeHwu3zse

# Hash the password using the generated salt
#hash = bcrypt.hashpw(senha.encode('utf-8'), salt)
hash = bcrypt.hashpw(senha, salt)
print(hash)
# $2a$08$K02Yy9Sn2mDReCeHwu3zseMpikne058OpGqfMhKHhuDLIYrnvNT9G


#import bcrypt

# Define the password
#senha = '12345'

# Generate a salt with a cost factor of 8
#salt = bcrypt.gensalt(8)

# Print the generated salt
#print(salt)

# Hash the password using the generated salt
#hash = bcrypt.hashpw(senha.encode('utf-8'), salt)

# Print the generated hash
#print(hash)