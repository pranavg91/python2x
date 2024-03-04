def make(*toppings):
    print(toppings)

make("panner")
make("panner","mushroom")
make("panner","mushroom","tomotto")


def make_base(*toppings,base):
    print("topping", toppings,"base", base)


make_base("mushroom","onion",base="Thin")