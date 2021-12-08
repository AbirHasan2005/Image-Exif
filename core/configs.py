# (c) @AbirHasan2005


class Colors(object):
    st = "\033[1;"  # Bold Style
    RED___ = f"{st}31;40m"
    GREEN_ = f"{st}32;40m"
    YELLOW = f"{st}33;40m"
    BLUE__ = f"{st}34;40m"
    PURPLE = f"{st}35;40m"
    CYAN__ = f"{st}36;40m"
    WHITE_ = f"{st}37;40m"



class Config(object):
    ENTER_IMAGE_PATH = f"\n{Colors.GREEN_}Enter Image Path: {Colors.CYAN__}"
    CHOOSE_FROM_MENU = "\n"
                       f"\n{Colors.GREEN_}[{Colors.YELLOW}01{Colors.GREEN_}] Get Exif Data"
                       f"\n{Colors.GREEN_}[{Colors.YELLOW}02{Colors.GREEN_}] Destroy Exif Data"
                       f"\n{Colors.GREEN_}[{Colors.YELLOW}00{Colors.GREEN_}] Exit Script"
                       "\n"
                       f"\n{Colors.GREEN_}Choose an option: {Colors.CYAN__}"
    
    @staticmethod
    def banner():
        BANNER = f"""{Colors.PURPLE}
 ___                              _____      _  __
|_ _|_ __ ___   __ _  __ _  ___  | ____|_  _(_)/ _|
 | || '_ ` _ \ / _` |/ _` |/ _ \ |  _| \ \/ / | |_
 | || | | | | | (_| | (_| |  __/ | |___ >  <| |  _|
|___|_| |_| |_|\__,_|\__, |\___| |_____/_/\_\_|_|
                     |___/{Colors.BLUE__}
                                v1.2  {Colors.CYAN__}
                                AbirHasan2005@GitHub
"""
        print("\033c")
        print(BANNER)
