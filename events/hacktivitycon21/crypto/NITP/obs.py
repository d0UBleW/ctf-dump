zero = "980ba27160cb23e950593ab153f3bc1ba077876672e79d26edfb77f16ae1c1407947e1dd8deb"
a = "f96ac31001aa428831385bd03292dd7ac116e6071386fc478c9a16900b80a021182680bcec8a"

zero = bytes.fromhex(zero)

for i in zero:
    print("{:02x}".format(i^b'a'[0]), end='')

print()
print(a)
