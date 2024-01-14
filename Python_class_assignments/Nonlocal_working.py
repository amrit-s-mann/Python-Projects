def outer():
    def inner():
                                        # <--- Note: There is no nonlocal keyword here.
                                        # Hence it doesn't change the x variable in outer()
        def inner2():
            nonlocal x                  # <--- Note: This references the x variable in inner()
                                        # It doesn't refer the x variable in outer()
            x = 2
            print("Inner2:", x)

        x = 3
        inner2()
        print("Inner:", x)

    x = 4
    inner()
    print("Outer:", x)                  # <--- Note: This x variable is not impacted by nonlocal
                                        # inside the inner2()

outer()