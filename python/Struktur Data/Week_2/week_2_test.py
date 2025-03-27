size = 3
dataset = []
top = -1
status = True

def push(data):
    global top, dataset
    if top == size - 1:
        print('Stack penuh')
    else:
        print(f"Data berhasil ditambahkan")
        dataset.append(data)
        top += 1
        
def pop():
    global top, dataset
    if top == - 1:
        print('Stack kosong')
    else:
        print("Data berhasil di pop")
        del dataset[top]
        top -= 1

def clear():
    global top
    top = - 1
    print("Dataset berhasil`di clear !")
    dataset.clear()

def peek():
    if dataset:
        print(f"Mengintip data {dataset[-1]}")
    else:
        print("Stack kosong")
        return None
 
while status == True:
    print('Dataset: '+ str(dataset))
    pilihan = int(input('Pilih: 1.Push | 2. Pop | 3. Clear | 4. Peek: '))
    if pilihan == 0:
        break
    elif pilihan == 1:
        a = input('Input data : ')
        push(a)
    elif pilihan == 2:
        pop()
    elif pilihan == 3:
        clear()
    elif pilihan == 4:
        peek()