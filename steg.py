from PIL import Image

TERMINATOR = '00000000'  # null terminator


def encode_image(img_path, message):
    img = Image.open(img_path).convert('RGB')
    binary_msg = ''.join(format(ord(c), '08b') for c in message) + TERMINATOR

    data = list(img.getdata())
    capacity = len(data) * 3
    if len(binary_msg) > capacity:
        raise ValueError('Message too long for this image')

    new_data = []
    msg_index = 0

    for pixel in data:
        r, g, b = pixel

        if msg_index < len(binary_msg):
            r = (r & ~1) | int(binary_msg[msg_index])
            msg_index += 1
        if msg_index < len(binary_msg):
            g = (g & ~1) | int(binary_msg[msg_index])
            msg_index += 1
        if msg_index < len(binary_msg):
            b = (b & ~1) | int(binary_msg[msg_index])
            msg_index += 1

        new_data.append((r, g, b))

    img.putdata(new_data)
    output_path = 'uploads/encoded.png'
    img.save(output_path)
    return output_path


def decode_image(img_path):
    img = Image.open(img_path).convert('RGB')
    data = list(img.getdata())

    binary_msg = ''
    for pixel in data:
        for color in pixel[:3]:
            binary_msg += str(color & 1)

    bytes_list = [binary_msg[i:i+8] for i in range(0, len(binary_msg), 8)]

    message_chars = []
    for byte in bytes_list:
        if byte == TERMINATOR:
            break
        if len(byte) < 8:
            break
        message_chars.append(chr(int(byte, 2)))

    return ''.join(message_chars)
