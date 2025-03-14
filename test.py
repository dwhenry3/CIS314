def namespace_test():
    x = 42

    print("Inner X:",id(x))
    print("Inner Int:",id(42))

x = 27

print("Outer X:",id(x))
print("Outer Int:",id(27))
namespace_test()