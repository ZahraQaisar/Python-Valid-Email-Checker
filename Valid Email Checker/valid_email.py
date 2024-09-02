def is_valid_email(em):
    find_at = em.find('@')
    find_dot = em.find('.')
    
    valid = 'Valid Email!'
    invalid = 'InValid Email!'
    if (len(em) > 0 or len(em) <= 256):
        if em[0].isalpha() or em[0].isalnum():
            if find_at != -1 and find_dot != -1:
                if em[em.index('@') + 1: em.index('.')].isalpha():
                    if len(em) - 1 != em.index('.'):   
                        after_dot = em.index('.') + 1
                        if em[after_dot].isalpha():
                            return valid
                        else:
                            return invalid
                    else:
                        return invalid
                else:
                    return invalid
            else:
                return invalid
        else:
            return invalid
    elif (len(em) <= 0 or len(em) > 256):
        print("Enter a valid email with with atleast 256 charactera.")

def main():
    email = input("Enter Email:")
    print(is_valid_email(email))

main()
