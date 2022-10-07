# ------------------- library -------------------
from enum import auto
import instaloader
import pyfiglet
from colorama import init, Fore

init()
import os
import webbrowser

# ------------------------------------------------

# ------------------- Setting ------------------- 
loader_connect = instaloader.Instaloader()

print(Fore.RED + "Step1: Please connect to your instagram account with user and password ")
print(Fore.CYAN + "-----------------------------------------------------------------")
user_instagram = input("Please enter of your instagram user account:")
print(Fore.CYAN + "-----------------------------------------------------------------")
pass_instagram = input("Please enter of your instagram password account:")
print(Fore.CYAN + "-----------------------------------------------------------------")
print(Fore.MAGENTA + "Please wait to connecting of your instagram account ...")

loader_connect.login(user_instagram, pass_instagram)

os.system('cls' if os.name == 'nt' else 'clear')

# ------------------- main page -------------------
menu_main = "1"
while menu_main == "1":
    def menu_get():
        print(Fore.LIGHTWHITE_EX + "-----------------------------------------------------------------")
        print("1 -> Back to menu")
        print("2 -> Exit")
        menu_page = input("[Enter number]~$")
        if menu_page == "1":
            pass
        elif menu_page == "2":
            exit()
        else:
            print(Fore.WHITE + "-----------------------------------------------------------------")
            print(Fore.LIGHTBLUE_EX + "[Enter number]~$ Please just enter number of menu.")
            menu_get()


    os.system('cls' if os.name == 'nt' else 'clear')
    txt = pyfiglet.figlet_format('Insta Bio')

    print(Fore.BLUE + txt)

    print(Fore.WHITE + "-----------------------------------------------------------------")

    print(Fore.YELLOW + "1 -> Biography")
    print(Fore.YELLOW + "2 -> Show Profile Photo")
    print(Fore.YELLOW + "3 -> Information of account")
    print(Fore.YELLOW + "4 -> Download All Posts")
    print(Fore.YELLOW + "5 -> Download All Stories and Profile Photo")
    print(Fore.YELLOW + "6 -> About programmer")
    print(Fore.YELLOW + "7 -> Donate Me a Coffee and ...")
    print(Fore.YELLOW + "8 -> Exit")
    print(Fore.WHITE + "-----------------------------------------------------------------")
    menu = input(Fore.WHITE + "[Enter number]~$")
    print(Fore.WHITE + "-----------------------------------------------------------------")

    # ------------------- main page -------------------

    # ------------------- biography  -------------------

    if menu == "1":
        id = input("please enter instagram account id with out @ :")
        print(Fore.GREEN + "-----------------------------------------------------------------")
        profile = instaloader.Profile.from_username(loader_connect.context, f"{id}")
        bio = profile.biography
        print(f"account biography of {id} is -----> {bio}")
        print(Fore.GREEN + "-----------------------------------------------------------------")
        menu_get()

        # ------------------- Profile Photo -------------------

    if menu == "2":
        id = input("please enter instagram account id with out @ :")
        print(Fore.GREEN + "-----------------------------------------------------------------")
        profile = instaloader.Profile.from_username(loader_connect.context, f"{id}")
        profile_pic = profile.profile_pic_url
        webbrowser.open(f'{profile_pic}')
        menu_get()

    if menu == "3":

        print(Fore.LIGHTMAGENTA_EX + "-----------------------------------------------------------------")
        print("1 -> Check private")
        print("2 -> Post count")
        print("3 -> Get follower (Max 200 or 300 Follower)")
        print("4 -> External link")
        print(Fore.LIGHTMAGENTA_EX + "-----------------------------------------------------------------")
        menu2 = input(Fore.WHITE + "[Enter number]~$")

        if menu2 == "1":
            print(Fore.WHITE + "-----------------------------------------------------------------")
            id = input("please enter instagram account id with out @ :")
            print(Fore.GREEN + "-----------------------------------------------------------------")
            profile = instaloader.Profile.from_username(loader_connect.context, f"{id}")
            private = profile.is_private
            print(Fore.LIGHTMAGENTA_EX + "-----------------------------------------------------------------")
            print(f"account {id} is private:{private}")
            menu_get()
        elif menu2 == "2":
            print(Fore.WHITE + "-----------------------------------------------------------------")
            id = input("please enter instagram account id with out @ :")
            print(Fore.GREEN + "-----------------------------------------------------------------")
            profile = instaloader.Profile.from_username(loader_connect.context, f"{id}")
            media = profile.mediacount
            print(f"post count of {id} account is : {media}")
            menu_get()
        elif menu2 == "3":
            print(Fore.WHITE + "-----------------------------------------------------------------")
            id = input("please enter instagram account id with out @ :")
            print(Fore.GREEN + "-----------------------------------------------------------------")
            profile = instaloader.Profile.from_username(loader_connect.context, f"{id}")


            #  followers_insta = []

            def follower_insta():
                followers = profile.get_followers()
                count = 0
                while count < 1:
                    yield list(followers)
                    count += 1


            for follower in follower_insta():
                for follower_i in follower:
                    print(follower_i)
            menu_get()


        elif menu2 == "4":
            print(Fore.WHITE + "-----------------------------------------------------------------")
            id = input("please enter instagram account id with out @ :")
            print(Fore.GREEN + "-----------------------------------------------------------------")
            profile = instaloader.Profile.from_username(loader_connect.context, f"{id}")
            url = profile.external_url
            print(f"External link : {url}")
            print(Fore.GREEN + "-----------------------------------------------------------------")
            menu_get()

    if menu == "4":
        id = input("please enter instagram account id with out @ :")
        profile = instaloader.Profile.from_username(loader_connect.context, f"{id}")

        for post in profile.get_posts():
            loader_connect.download_post(post, target="instabio")

    if menu == "5":
        id = input("please enter instagram account id with out @ :")
        profile = instaloader.Profile.from_username(loader_connect.context, f"{id}")
        loader_connect.download_profile(id, download_stories_only=True)
        print(Fore.LIGHTGREEN_EX + "All Stories and Profile Photo Downloaded.")
        menu_get()

    if menu == "6":
        print(Fore.BLUE + "-----------------------------------------------------------------")
        print(Fore.LIGHTYELLOW_EX + "Programmer : Zero0zed")
        print(Fore.LIGHTYELLOW_EX + "Telegram channel : @Zero00zed")
        print(Fore.LIGHTYELLOW_EX + "Github Username : Zero0zed")
        print(Fore.BLUE + "-----------------------------------------------------------------")
        menu_get()

    if menu == "7":
        webbrowser.open("https://coffeebede.ir/zerozed")
        menu_get()

    if menu == "8":
        exit()
