def sponge_case(sentence):
    # Write your solution here!
    word_arr = sentence.split()
    new_arr = []

    for word in word_arr:
        scramble = ""
        for i, letter in enumerate(word):
            if i % 2 == 0:
                scramble += letter.lower()
            else:
                scramble += letter.upper()
        new_arr.append(scramble)
    return (' ').join(new_arr)


# Test cases
# assert sponge_case("spongebob") == "sPoNgEbOb"
assert sponge_case("Who are YOU calling A Pinhead") == "wHo aRe yOu cAlLiNg a pInHeAd"
assert sponge_case("WHAT is UP my dude") == "wHaT iS uP mY dUdE"
assert sponge_case("E") == "e"
assert sponge_case("e") == "e"

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")
