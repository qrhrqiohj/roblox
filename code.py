from colorama import Fore, Style, init
init()
import importlib.util
import os

# user guide for making your own
# addon/addon2 will set replacee/replacement to a string. addon can be a list (optional), addon2 cant
# start_key/start_key2 will start the user in a json from a set position (make sure the set position doesnt share a name or ill go to the first one)
# return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names finishes an area and returns all the data back and finishes this codes use
# add a line push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names) for doing multiple changes of seperate things in the same case
# if you want to skip then set skip to True
# leaving empty and only returning will make the user enter 2 from the json starting from the top

def get_valid_input(prompt, valid_values=None):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'back':
            return 'back'
        try:
            if valid_values is None or int(user_input) in valid_values:
                return int(user_input)
            else:
                print(f"{Fore.RED}\nInvalid option. Please choose from {valid_values}.\n{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}\nInvalid input. Please enter a valid number.\n{Style.RESET_ALL}")


def push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names):
    spec = importlib.util.spec_from_file_location("backbone_module", "main.py")
    backbone_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(backbone_module)

    if hasattr(backbone_module, "backbone"):
        json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names = backbone_module.backbone(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
    else:
        print(f"Error: The file {backbone_module} does not contain a `backbone` function.")


def run(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names):

    while True:
        options = get_valid_input(f"Asset replacements:\n"
                        f"0:  {Fore.GREEN}Custom{Style.RESET_ALL}\n"
                        f"1:  {Fore.GREEN}No Textures{Style.RESET_ALL}\n"
                        #f"10:  {Fore.GREEN}R6 Noclip{Style.RESET_ALL}\n"
                        f"Type 'back' to return to the previous menu.\n: ",
                        valid_values=[0, 1]
        )
        if options == 'back':
            print(f"{Fore.CYAN}\nReturning to main menu.{Style.RESET_ALL}")
            skip = True
            return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
        
        try:
            match options:
                case 0:
                    return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                case 1:
                    addon = ['0929fa96e057727f17934aadd5a18654', '0c6deb1bc158cc099db53ac300d952a7', '115f92fa561eef93e549001dab3f4890', '19ece9db762c10026a64e078c6eaf735', '1ae474d121bdf012593d22e7bd5e9854', '1c56425cccf76c88b707bcf7196ec2fb', '369bdc60330f0dd596a0ee281b12c5c9', '3ebdcfc63270d66a6594028c278913b5', '4531929c30a509d6a16e655cdd918af9', '48b7e16ffb6d1ca71bd21a47234d0bbc', '6ace0cd56ca5e293a9f87d9b652f7690', '7d2d09489b90c07e07f0dc923f118f61', '7f88cccd1130e907b7ee96f2b90555ad', '85fad2384eb1fcbaf4ccebc2c8d7c84d', '9483c5b01fbaaa6bcc97060d0cb0402f', 'b1c7ea393774f19f9ed47f21e453a0f2', 'b35db36d16e3ac477de529c1908621a0', 'b8f898ff9aadaee800d07054ef91a769', 'c0975ad2729339e86a60acac5e5d5867', 'c10c9f476fa22a56b840b540807d2f89', 'c1435eb5d3b6ed586ba64f941a6ba811', 'c314fa6eb570bda8e19619e3c1d9d2b7', 'ce07937636c1d66eb9db095dd0098b37', 'cfd0d20b94d7e7ced1a18aa270410d50', 'eb7d542844ec8de99dbf63a2259b6dc9', 'effba77eb3c7df2880f456ad147e1e7d', 'f271a6006decc23bf95a7eedef909e94', 'f8e86703186511d89859e2b63d169989', 'fe0ea6c9a2f560fdc7005c3c02c71dce', 'ff874e07a882070ea5cb0c3369e4d269']
                    addon2 = "ffc3fc61237335e80db176e2827ed1ed"
                    return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                #case 10:
                    #addon = ['a2f3fad0cecf63e774e8ef6cc9c97b4e', 'd20f0d3583c732a8051c2158f5cc1f19', '0fd5f9c25cd37c70ef6e684c72074e49', '22a87dc2fcc1d7f2d4eebec174141c11', '7539c4f54a00b625bdbd7d7a7e7ef8f1']
                    #addon2 = "ffc3fc61237335e80db176e2827ed1ed"
                    #return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
        except Exception as e:
            print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")
