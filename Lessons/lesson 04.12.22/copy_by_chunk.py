filename = "test.jpg"
new_filename = filename.split('.')
new_filename[0] += "_copy"
new_filename = '.'.join(new_filename)

chunk = 1000
counter = 0
with open(filename, 'rb') as donor:
    with open(new_filename, 'wb') as receiver:
        while True:
            c = donor.read(chunk)
            if c:
                receiver.write(c)
                counter += 1
                print(counter)
            else:
                break