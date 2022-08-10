import argparse
from colorama import init, Fore
init(autoreset=True)


parser = argparse.ArgumentParser()
parser.add_argument('-t', type=str, default=None, required=True,
                    help='输入二进制文本')
args  = parser.parse_args()

cipher = args.t

def BintoAsc(cipher, bit, reverse=False):
    ascii_str = ""
    for i in range(0, len(cipher), bit):
        bin_str = cipher[i:i + bit][::-1] if reverse else cipher[i:i + bit]
        # 如果127 >= num >= 32,那就是可见字符,不可见字符统统转换为`~`(波浪线)
        ascii_str += chr(num) if 127 >= (num := int(bin_str, 2)) >= 32 else chr(126)
    return ascii_str

input_ = input(f"{Fore.GREEN}是否尝试0和1互换后转换Ascii码? (N/y):")
if input_ not in ["N", "n", ""]:
    cipher = "".join("1" if i == "0" else "0" for i in cipher)

# 正常情况
print(f"{Fore.RED} [7Bit]: {Fore.BLUE}{BintoAsc(cipher, 7)}")
print(f"{Fore.RED} [8Bit]: {Fore.BLUE}{BintoAsc(cipher, 8)}")
print()

# 特殊情况1
print(f"{Fore.YELLOW} [1].尝试全部字节倒序后转换Ascii码:")
reverse_cipher = cipher[::-1]
print(f"{Fore.RED}  [7Bit]: {Fore.BLUE}{BintoAsc(reverse_cipher, 7)}")
print(f"{Fore.RED}  [8Bit]: {Fore.BLUE}{BintoAsc(reverse_cipher, 8)}")
print()

# 特殊情况2
print(f"{Fore.YELLOW} [2].尝试每个字节依次倒序后转换Ascii码:")
print(f"{Fore.RED}  [7Bit]: {Fore.BLUE}{BintoAsc(cipher, 7, reverse=True)}")
print(f"{Fore.RED}  [8Bit]: {Fore.BLUE}{BintoAsc(cipher, 8, reverse=True)}")