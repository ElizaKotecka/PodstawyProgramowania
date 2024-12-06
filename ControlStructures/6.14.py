# Write a program that checks whether a given person is a good influencer,
# that is, whether the person has at least two of the following accounts: Facebook, Twitter or Instagram.

facebook = True
twitter = False
instagram = True

if (facebook + twitter + instagram) >= 2:
    print("You are a good influencer!")
else:
    print("You are not a good influencer.")