from midterm import Midterm,NAME,CT,Mathx, Atberti
from utilities import file_to_text

def get_info():
    try:
        print('{}'.format('-'*40))
        print('Name: {} {}'.format(Midterm.get_first_name(), Midterm.get_last_name()))
        print('ID: {}'.format(Midterm.get_ID()))
        print('filename = {}'.format(NAME))
        print()
        print(Midterm.get_certification())
        print('{}'.format('-'*40))
        print()
    except Exception as e:
        print('Exception by get_info: {}'.format(e))
    return

#Columnar Transposition
def test_task1():
    print('{}'.format('-'*40))
    print("Start of Task 1: Columnar Transposition Testing")
    print()
    
    try:
        cases = [1,2,3,4,5,6,7,8,9,10,None]
        print('Testing get_words:')
        for c in cases:
            print('len(get_words({})) = {}'.format(c,len(CT.get_words('engmix.txt',c))))
        print()
    except Exception as e1:
        print('Exception in test_task1:CT.get_words: {}'.format(e1))
    
    try:
        keys = ['',['a','b'],'a','aa','ABC','a$?a','psut','e-learning','conversations']
        words = CT.get_words('engmix.txt',None)
        print('Testing valid key:')
        for key in keys:
            print('valid_key({}) = {}'.format(key,CT.valid_key(key,words)))
        print()
    except Exception as e2:
        print('Exception in test_task1:CT.valid_key: {}'.format(e2))
    
    try:
        keys = ['aba','conversations','2cents','Jordan','smart city']
        print('Testing adjust_key:')
        for key in keys:
            print('adjust_key({}) = {}'.format(key,CT.adjust_key(key)))
        print()
    except Exception as e3:
        print('Exception in test_task1:CT.adjust_key: {}'.format(e3))
    
    try:
        keys = ['mark','smoothy','smart city','Jordan']
        print('Testing key_order:')
        for key in keys:
            print('key_order({}) = {}'.format(key,CT.key_order(key)))
        print()
    except Exception as e4:
        print('Exception in test_task1:CT.key_order: {}'.format(e4))

    try:
        print('Testing default constructor:')
        ct = CT()
        print(ct)
        print()
    except Exception as e5:
        print('Exception in test_task1:CT:default_constructor {}'.format(e5))
        return # if object creation fails, needs to return
    
    try:
        print('Testing set_pad and get_pad:')
        pads = ['xx',3,'$','Q','x']
        for p in pads:
            print('set_pad({}) = {}, get_pad = {}'.format(p,ct.set_pad(p), ct.get_pad()))
        print()
    except Exception as e6:
        print('Exception in test_task1:CT.set_pad & get_pad: {}'.format(e6))

    try:
        print('Testing set_key, get_key:')
        keys = [123, 'c', 'Jordan','jordan','successful']
        for k in keys:
            print('set_key({}) = {}, get_key = {}'.format(k,ct.set_key(k), ct.get_key()))
        print()
    except Exception as e7:
        print('Exception in test_task1:CT.set_key & get_key: {}'.format(e7))
    
    try:
        print('Testing encryption and decryption')
        keys = ['rat','fly','snake']
        plaintexts = ['ABCDEF','types of insects','This is a kind of reptiles']
        pads = ['r','q','x']
        for i in range(len(keys)):
            ct.set_key(keys[i])
            ct.set_pad(pads[i])
            print('key = {}, pad = {}'.format(ct.get_key(),ct.get_pad()))
            print('plaintext  = {}'.format(plaintexts[i]))
            ciphertext = ct.encrypt(plaintexts[i])
            print('ciphertext = {}'.format(ciphertext))
            plaintext2 = ct.decrypt(ciphertext)
            print('plaintext2 = {}'.format(plaintext2))
            print()
    except Exception as e8:
        print('Exception in test_task1:CT.encrypt & decrypt: {}'.format(e8))

    try:
        print('Testing cryptanalysis:')
        
        info = Midterm()
        print('Testing student file:')
        cipher_file = 'ciphertext1_' + NAME + '.txt'
        ciphertext = file_to_text(cipher_file)
        print('ciphertext = {}'.format(ciphertext[:50]))
        
        #This line is for slow testing
        #key,plaintext = CT.cryptanalyze(ciphertext,NAME)
        
        #These lines are for fast testing
        key,plaintext = info.get_task1_solution()

        print('plaintext  = {}'.format(plaintext[:50]))
        print('key = {}'.format(key))
        
    except FileNotFoundError:
        print('Exception: {} is not found'.format(cipher_file))
    except Exception as e9:
        print('Exception by Task 1: {}'.format(e9))
    finally:
        print()
                
    print('End of Task 1: Columnar Transposition Testing')
    print('{}'.format('-'*40))
    print()
    return

def test_task2():
    print('{}'.format('-'*40))
    print("Start of Task 2: Mathx Testing")
    print()

    try:        
        print('Testing Mathx.valaid_key')
        cases = [[5,2,3,28],(2,1,0),(1,3.2,4,32),(3,7,-6,34),(3,7,6,27),(12,9,13,16),
                 (8,7,15,66),(0,1,1,36),(94,16,17,38)]
        for c in cases:
            print('{:20s} --> {}'.format(str(c), Mathx.valid_key(c)))
        print()
    except Exception as e1:
        print('Exception in Testing Mathx.valid key: {}'.format(e1))

    try:
        print('Testing default constructor:')
        mcipher = Mathx()
        print(mcipher)
        print()
    except Exception as e2:
        print('Exception in Testing Mathx.default Constructor: {}'.format(e2))
        
    try:    
        print('Testing basic methods:')
        keys = [(3,8,9,38),(12,9,13,16),(0,1,1,36),(94,16,17,40),(1,2,3,42),(3,5,0,44)]
        for key in keys:
            print('key = {}'.format(key))
            print('Setting Mathx key to {}'.format(key))
            print('\tset_key success = {}'.format(mcipher.set_key(key)))
            print('\tget_key = {}'.format(mcipher.get_key()))
            print('\tget_base = {}'.format(mcipher.get_base()))
            print('\tget_type = {}'.format(mcipher.get_type()))
            print('\t{}'.format(mcipher))

            print()
    except Exception as e3:
        print('Exception in Testing Mathx basics: {}'.format(e3))    
    
    try:    
        print('Testing Encryption and Decryptoin')
    
        plaintexts = ['Strike in progress', 'DECIMATION CIPHER','mission accomplished?', 
                      'Mission Failed!', 'Silly Key','Caesar Cipher']
        keys = [(3,3,0,46),(2,2,0,44),(1,2,3,52),(14,16,17,50),(12, 9, 13, 16),
                (16,2,1,28)]
    
        for i in range(len(keys)):
            k = keys[i]
            plaintext = plaintexts[i]
            mcipher.set_key(k)
            print(mcipher)
            print('plaintext =  ', plaintext)
            ciphertext = mcipher.encrypt(plaintext)
            print('ciphertext=  ',ciphertext)
            plaintext2 = mcipher.decrypt(ciphertext)
            print('plaintext2=  ',plaintext2)
            print()
    except Exception as e4:
        print('Exception in Task2.Mathx.encrypt & decrypt: {}'.format(e4))
    
    try:
        #This block is for your own testing
        # print('----------- cryptanalysis on sample data:')
        # plaintext = 'there are two kinds of cryptography in this world: '
        # plaintext += 'cryptography that will stop your kid sister from reading your files, '
        # plaintext += 'and cryptography that will stop major governments from reading your files.'
        
        # mcipher.set_key((1,2,3,52))
        # ciphertext = mcipher.encrypt(plaintext)
        # print('plaintext  = {}'.format(plaintext))
        # print('ciphertext = {}'.format(ciphertext))
        # key,plaintext2 = Mathx.cryptanalyze(ciphertext)
        # print('plaintext2 = {}'.format(plaintext2.lower()))
        # print('key = {}'.format(key))
        # print()
    
        print('Testing cryptanalysis on student file:')
        
        info = Midterm()
        print('Testing student file:')
        cipher_file = 'ciphertext2_' + NAME + '.txt'
        ciphertext = file_to_text(cipher_file)
        print('ciphertext = {}'.format(ciphertext[:50]))
        
        #This line is for slow testing
        #key,plaintext = Mathx.cryptanalyze(ciphertext,NAME)
        
        #These lines are for fast testing
        key,plaintext = info.get_task2_solution()
        
        print('plaintext  = {}'.format(plaintext[:50]))
        print('key = {}'.format(key))
        
    except FileNotFoundError:
        print('Exception: {} is not found'.format(cipher_file))
    except Exception as e9:
        print('Exception by Task 2: {}'.format(e9))
    finally:
        print()
    
    print('End of Task 2: Mathx Testing')
    print('{}'.format('-'*40))
    print()
    return

def test_task3():
    print('{}'.format('-'*40))
    print("Start of Task 3: Atberti Testing")
    print()

    try:        
        print('Testing Atberti.valaid_key')
        cases = [['lower','p'],('lower','p','k'),(15,'k'),('upper',20.2),
                 ('ascii','r'),('BA','mr'),('B6','$'),('alpha','L'),('B6',' ')]
        for c in cases:
            print('{:20s} --> {}'.format(str(c), Atberti.valid_key(c)))
        print()
    except Exception as e1:
        print('Exception in Testing Atberti.valid key: {}'.format(e1))
        
    try:
        print('Testing default constructor:')
        atberti = Atberti()
        print(atberti)
        print()
    except Exception as e2:
        print('Exception in Testing Atberti.default Constructor: {}'.format(e2))
        
    try:    
        print('Testing basic methods:')
        keys = [('lower','k'),('alpha','M'),('alphanum','4'),('pascii','r'),
                ('html','P')]
        for key in keys:
            print('set_key({}) = {}'.format(key,atberti.set_key(key)))
            print('get_key() = {}'.format(atberti.get_key()))
            out_wheel,in_wheel = atberti.get_wheels()
            print('out_wheel = {}'.format(out_wheel))
            print('in_wheel  = {}'.format(in_wheel))
            print()
    except Exception as e3:
        print('Exception in Testing Atberti basics: {}'.format(e3))    

    try:    
        print('Testing Encryption and Decryptoin')
    
        plaintext1 = 'Gaza Remains in Our Hearts!' 
        plaintext2 = 'Alberti + Atbash = Atberti'
        plaintext3 = 'Cryptography to some is an art not science'
        plaintext4 = 'One must acknowledge with cryptography '
        plaintext4 += 'no amount of violence will ever solve a math problem.'
        plaintexts = [plaintext1,plaintext2,plaintext3,plaintext4]
    
        keys = [('alpha','G'),('BA','+'),('lower','s'),('alphanum','R')]
    
        for i in range(len(keys)):
            k = keys[i]
            plaintext = plaintexts[i]
            atberti.set_key(k)
            print(atberti)
            print('plaintext =  ', plaintext)
            ciphertext = atberti.encrypt(plaintext)
            print('ciphertext=  ',ciphertext)
            plaintext2 = atberti.decrypt(ciphertext)
            print('plaintext2=  ',plaintext2)
            print()
    except Exception as e4:
        print('Exception in Task3.Atberti.encrypt & decrypt: {}'.format(e4))

    try:
        #This block is for your own testing
        # print('cryptanalysis on sample data:')
        # plaintext = 'there are two kinds of cryptography in this world: '
        # plaintext += 'cryptography that will stop your kid sister from reading your files, '
        # plaintext += 'and cryptography that will stop major governments from reading your files.'
        #
        # atberti.set_key(('lower','m'))
        # ciphertext = atberti.encrypt(plaintext)
        # print('plaintext  = {}'.format(plaintext))
        # print('ciphertext = {}'.format(ciphertext))
        # key,plaintext2 = atberti.cryptanalyze(ciphertext)
        # print('plaintext2 = {}'.format(plaintext2.lower()))
        # print('key = {}'.format(key))
        # print()
    
        # print('Testing cryptanalysis on student file:')
        
        info = Midterm()
        print('Testing student file:')
        cipher_file = 'ciphertext3_' + NAME + '.txt'
        ciphertext = file_to_text(cipher_file)
        print('ciphertext = {}'.format(ciphertext[:50]))
        
        #This line is for slow testing
        #key,plaintext = atberti.cryptanalyze(ciphertext)
        
        #These lines are for fast testing
        key,plaintext = info.get_task3_solution()
        
        print('plaintext  = {}'.format(plaintext[:50]))
        print('key = {}'.format(key))
        
    except FileNotFoundError:
        print('Exception: {} is not found'.format(cipher_file))
    except Exception as e5:
        print('Exception by Task 3: {}'.format(e5))
    finally:
        print()
                           
    print('End of Task 3: Atberti Testing')
    print('{}'.format('-'*40))
    print()
    return
    
get_info()
test_task1()
test_task2()
test_task3()
