import hashlib

# file to create password for
path = r'C:\Users\userTK427\Desktop\Workspaces\Python\env1\Scripts\example.txt'

# setting the hashing
# with open(path, 'rb') as opened_file:
#     content = opened_file.read()
#     md5 = hashlib.md5()
#     sha1 = hashlib.sha1()
#     sha224 = hashlib.sha224()
#     sha256 = hashlib.sha256()
#     sha384 = hashlib.sha384()
#     sha512 = hashlib.sha512()
#
#     md5 = update(content)
#     sha1 = update(content)
#     sha224 = update(content)
#     sha256 = update(content)
#     sha384 = update(content)
#     sha512 = update(content)
#
#     print('Result')
#     print()
#     print('{}: {}'.format(md5.name, md5.hexidigest()))
#     print('{}: {}'.format(sha1.name, sha1.hexidigest()))
#     print('{}: {}'.format(sha224.name, sha224.hexidigest()))
#     print('{}: {}'.format(sha256.name, sha256.hexidigest()))
#     print('{}: {}'.format(sha384.name, sha384.hexidigest()))
#     print('{}: {}'.format(sha512.name, sha512.hexidigest()))

md5 = hashlib.md5()
sha1 = hashlib.sha1()
sha224 = hashlib.sha224()
sha256 = hashlib.sha256()
sha384 = hashlib.sha384()
sha512 = hashlib.sha512()

list_hash_objects = [sha256]

with open(path, 'rb') as opened_file:
    print('Result')
    print()
    content = opened_file.read()
    for hash_object in list_hash_objects:
        hash_object.update(content)
        print('{}: {}'.format(hash_object.name, hash_object.hexdigest()))

# for hash_object in list_hash_ojects:
#     with open(path, 'rb') as opened_file:
#         for line in opened_file:
#             hash_object.update(line)
#         print('{}: {}'.format(hash_object.name, hash_object.hexdigest()))









#
