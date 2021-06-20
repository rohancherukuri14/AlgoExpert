def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    if fastest:
        redShirtSpeeds.sort(reverse=True)
    else:
        redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    total = 0
    for i in range(0, len(redShirtSpeeds)):
        total += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return total