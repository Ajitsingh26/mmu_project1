from select_friend import select_friend
from steganography.steganography import Steganography

def send_message():
    friend_choice=select_friend()
    original_image=raw_input("provide the name of the image to hide the message")
    output_image=raw_input("provide the name of the output image")
    text=raw_input('enter your text here')

    Steganography.encode(original_image, output_image, text)

    print "your message is encrypted..!"


