import base64

def base64_encode(text):
    try:
        encoded_bytes = base64.b64encode(text.encode('utf-8'))
        return encoded_bytes.decode('utf-8')
    except Exception as e:
        return f"Encoding error: {e}"

def base64_decode(encoded_text):
    try:
        decoded_bytes = base64.b64decode(encoded_text.encode('utf-8'))
        return decoded_bytes.decode('utf-8')
    except Exception as e:
        return f"Decoding error: {e}"

def test_base64():
    print("Base64 Encode/Decode Test:")
    sample_text = "Crypto Challenge Day 3"
    encoded = base64_encode(sample_text)
    decoded = base64_decode(encoded)
    print(f"Original: {sample_text}")
    print(f"Encoded : {encoded}")
    print(f"Decoded : {decoded}")
