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
                        f"1:  {Fore.GREEN}R6 Noclip{Style.RESET_ALL}\n"
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
                    addon = ['a2f3fad0cecf63e774e8ef6cc9c97b4e', 'd20f0d3583c732a8051c2158f5cc1f19', '0fd5f9c25cd37c70ef6e684c72074e49', '22a87dc2fcc1d7f2d4eebec174141c11', '7539c4f54a00b625bdbd7d7a7e7ef8f1']
                    addon2 = "ffc3fc61237335e80db176e2827ed1ed"
                    return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
        except Exception as e:
            print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")
