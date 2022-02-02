email = input('What is the email address?:').strip()
user_name = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
res = "Your username is '{}' and your domain name is '{}' ".format(user_name,domain_name)
print(res)
