def main():
    i = 0
    while i < 3:
        word1 = input("Enter a new password:\n ")
        if validatePassword(word1):
            word2 = input("Please re-enter the same password: ")
            if word1 != word2:
                print("Passwords do not match!")
            else:
                print("Password is valid and two entries are matching")
                break
        else:
            print("your password does not meet complexity requirements")
        i = i + 1
    else:
        print("You have not provided a valid password, goodbye!")


def validatePassword(pw):
    if not pw.isalnum() or len(pw) < 8 or pw.isupper() or pw.islower() or pw.isdigit():
        return False
    else:
        return True


main()

# word1 = input("Enter a new password:\n ")
# i = 0
# if validatePassword(word1):
#     # word2 = input("Please re-enter the same password: ")
#     # i = 0
#     while i <= 3:
#         word2 = input("Please re-enter the same password: ")
#         if word1 != word2:
#             print("Passwords do not match!")
#     # i = i + 1
#
#         # if i == 3:
#         #     return "You have not provided a valid password, goodbye!"
#
#         else:
#             return "Password is valid and two entries are matching"
#
#     i = i + 1
# if i == 3:
#     return "You have not provided a valid password, goodbye!"
# else:
#     print("Your password does not meet complexity requirements!")
# word1 = input("Enter a new password:\n ")
