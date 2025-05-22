def rail_fence_encrypt(text, rails):
    if rails <= 1:
        return text

    fence = ['' for _ in range(rails)]
    rail = 0
    direction = 1

    for char in text:
        fence[rail] += char
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    return ''.join(fence)


def rail_fence_decrypt(cipher, rails):
    if rails <= 1:
        return cipher

    # Build the zigzag pattern indexes
    pattern = list(range(rails)) + list(range(rails - 2, 0, -1))
    indexes = [0] * len(cipher)
    rail_len = [0] * rails

    idx = 0
    for i in range(len(cipher)):
        r = pattern[idx % len(pattern)]
        rail_len[r] += 1
        idx += 1

    # Fill each rail with the right number of characters
    rails_content = []
    pos = 0
    for r in rail_len:
        rails_content.append(cipher[pos:pos + r])
        pos += r

    # Reconstruct original message
    result = ''
    rail_indices = [0] * rails
    idx = 0
    for i in range(len(cipher)):
        r = pattern[idx % len(pattern)]
        result += rails_content[r][rail_indices[r]]
        rail_indices[r] += 1
        idx += 1

    return result
