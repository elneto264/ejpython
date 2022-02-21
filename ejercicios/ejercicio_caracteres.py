def mCar(words):
    pos=0
    for x in range(len(words)):
        if len(words[x])>len(words[pos]):
            pos=x
    return words[pos]

words=["khskg", "ouwoifs", "klsdflks", "uwyrs", "ljdfklsjdf", "lñslfs"]
print("Palabra con mas caracteres ",mCar(words))