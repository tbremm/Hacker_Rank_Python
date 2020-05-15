# You are given an integer N followed by N email addresses. Your task is to print a list containing only valid email
# addresses in lexicographical order. Valid email addresses must follow these rules:
#
# It must have the username@websitename.extension format type.
# The username can only contain letters, digits, dashes and underscores.
# The website name can only have letters and digits.
# The maximum length of the extension is .
#
# Concept
# A filter takes a function returning True or False and applies it to a sequence, returning a list of only those
# members of the sequence where the function returned True. A Lambda function can be used with filters.
# Let's say you have to make a list of the squares of integers from 0 to 9 (both included).
#
# >> l = list(range(10))
# >> l = list(map(lambda x:x*x, l))
#
# Now, you only require those elements that are greater than 10 but less than 80.
#
# >> l = list(filter(lambda x: x > 10 and x < 80, l))
#
# Input Format
# The first line of input is the integer N, the number of email addresses.
# N lines follow, each containing a string.
#
# Constraints
# Each line is a non-empty string.
#
# Output Format
# Output a list containing the valid email addresses in lexicographical order. If the list is empty, just output an
# empty list, [].


# The username can only contain letters, digits, dashes and underscores
def is_username_valid(un):
    un = un.replace('-', '')  # Hyphens are allowed
    un = un.replace('_', '')  # Underscores are allowed
    return un.isalnum()


# Returns true if the domain is alphanumeric
def is_domain_valid(domain):
    return domain.isalnum()


def is_ext_valid(ext):
    return ext.isalnum() and len(ext) <= 3


def is_email_valid(email):
    # return True if email is a valid email, else return False
    first_split = email.split('@')  # Get the username first (username[0])
    if len(first_split) != 2:  # We have more or less than one '@' - not allowed
        print('not exactly one @')
        return False
    if not is_username_valid(first_split[0]):
        print('un invalid')
        return False
    second_split = first_split[1].split('.')  # Get the domain (second_split[0]) and ext (second_split[1])
    if len(second_split) != 2:  # Can't have more or less than one '.'
        print('Not exactly one .')
        return False
    if not is_domain_valid(second_split[0]):
        print('Domain invalid')
        return False
    if not is_ext_valid(second_split[1]):
        print('Ext invalid')
        return False
    return True


def filter_mail(emails):
    return list(filter(is_email_valid, emails))


n = int(input())
email_list = []
for _ in range(n):
    email_list.append(input())

filtered_emails = filter_mail(email_list)
filtered_emails.sort()
print(filtered_emails)
