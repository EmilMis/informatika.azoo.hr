from User.Error import error_message

colors = {
    "RED": '\033[1;31m',
    "RESET": '\033[0;0m',
    "BLUE": '\033[1;34m'
}


def format_c(text, color):
    if text == error_message:
        return f"{colors['RED']}{error_message}{colors['RESET']}"
    else:
        return f"{colors[color]}{text}{colors['RESET']}"
