browser = input("which browser you want to use\n")

run=browser.lower()
print(run)
match run:
    case "chrome":
        print("Execute script in chrome")
    case "edge":
        print("Execute script in Edge")
    case "safari":
        print("Execute script in saafari")
    case _:
        print("default browser is used")

