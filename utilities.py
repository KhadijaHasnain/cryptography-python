from math import ceil

ENCODINGS = ['lower','upper','alpha','lowernum','uppernum','alphanum',
             'special','nonalpha','B6','BA','pascii','unicode128','unicode256']
ENGLISH_FREQ = [0.08167,0.01492,0.02782, 0.04253, 0.12702,0.02228, 0.02015,
                0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
                0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
                0.00978, 0.0236, 0.0015, 0.01974, 0.00074]
HACK_DICT = 'engmix.txt'
PAD = 'q'

'______________________________________________________________________________'

def get_base(encoding):
    """
    ----------------------------------------------------
    Parameters:   encoding (str) 
    Return:       result (str)
    Description:  Return string containing all characters defined in the given encoding
                  Defined base types:
                      lower: lower case characters
                      upper: upper case characters
                      alpha: upper and lower case characters
                      lowernum: lower case and numerical characters
                      uppernum: upper case and numerical characters
                      alphanum: upper, lower and numerical characters
                      special: punctuation and special characters (no white spaces)
                      nonalpha: special and numerical characters
                      B6: num, lower, upper, space and newline
                      BA: upper + lower + num + special + ' \n'
                      pascii: upper, lower, numerical and special characters
                      unicode128: pascii + few unicode characters
                      unicode256: pascii + many unicode characters
    Errors:       if invalid encoding, print error msg, return empty string
    ---------------------------------------------------
    """
    lower = "".join([chr(ord('a')+i) for i in range(26)])
    upper = lower.upper()
    num = "".join([str(i) for i in range(10)])
    alpha = upper + lower
    special = ''
    for i in range(ord('!'),127):
        if not chr(i).isalnum():
            special+= chr(i)
    
    unicode1 = 'ÄÆÑÓÙÝäß£¥Ø±÷«»×©ŖŴŽģΔΓΠΦΨδϪΩω¶♤∫₡'
    unicode2 = '❤♫☎♨✈☀✂☑✉☆✎♕✍♂♀ϨϾЊжѠ😀😂😌😛😣😎😔😥😱😬😳😸🙄🙈🙌🙏😈✌❌➔➶🌍🌩🌭🌽🍉🌲🍄🍔🍩🍼🍽🎒🎧'
    unicode2 += '⚙⚠⚰⚽⚿⛍⛔⛏⛵⛷🎤⚀⚂⚄♲⚓⚖∋∌∛∧∨∩∪∲∴∵∻≂≄≡≤≥⊂⊃⊄⊞⊠⊤⊥⊻⊼⊿⋇⋈⋉⋐⋓▦◐◍◢◥◪◆◎☂☃☍☁☕☝☠☢☪☹☺♔♖♙♘🎮🏍🏠'
    result = ''
    if encoding == 'lower': #26 chars
        result = lower
    elif encoding == 'upper': #26 chars
        result = upper
    elif encoding == 'alpha': #52 chars
        result = alpha
    elif encoding == 'lowernum': #36 chars
        result = lower + num
    elif encoding == 'uppernum': #36 chars
        result = upper + num
    elif encoding == 'alphanum': #62
        result = alpha + num
    elif encoding == 'special': #32 chars
        result = special
    elif encoding == 'nonalpha': #42
        result = special + num
    elif encoding == 'B6': #64 symbols
        result = alpha + num + ' ' + '\n'
    elif encoding == 'BA': #96 symbols
        result = alpha + num + special + ' \n'
    elif encoding == 'pascii': #94 printable ASCII characters
        result = alpha + num + special
    elif encoding == 'unicode128': #128
        result = alpha + num + special + unicode1
    elif encoding == 'unicode256': #256 chars
        result = alpha + num + special + unicode1 + unicode2
    else:
        print('Error(get_chars): undefined base type')
        result = ''
    return result

'______________________________________________________________________________'
def get_str_blocks(string,block_size,pad =''):
    """
    ----------------------------------------------------
    Parameters:   string (str): input string
                  block_size (int)
                  pad (str): padding character, by default empty string (no padding)
    Return:       blocks (list)
    Description:  Create a list containing strings each of given block size
                  if padding used, pad last block with given character
    Asserts:      string is str and block_size is a positive integer
                    pad is an empty string or a single character
    ---------------------------------------------------
    """
    assert type(string) == str, 'invalid string'
    assert type(block_size) == int and block_size > 0, 'invalid block size'
    assert type(pad) == str and (pad == '' or len(pad) == 1), 'invalid pad'
    
    s = string
    b = block_size
    blocks = [s[i*b:(i+1)*b] for i in range(ceil(len(s)/b))]
    
    if pad != '':
        if (len(blocks) == 1 and len(blocks[0]) < b) or \
            len(blocks) > 1 and len(blocks[-1]) < len(blocks[0]):
                blocks[-1] += pad*(b - len(blocks[-1]))
    
    return blocks

'______________________________________________________________________________'
def load_hack_dictionary(dictionary_file=HACK_DICT):
    """
    ----------------------------------------------------
    Parameters:   dictionary_file (str): filename
    Return:       dict_list (list): 2D list
    Description:  Reads a given dictionary file
                  dictionary is assumed to be formatted as each word in a separate line
                  Returns a list of lists, list 0 contains all words starting with 'a'
                  list 1 all words starting with 'b' and so forth.
    Errors:       if invalid filename, print error msg, return []
    ---------------------------------------------------
    """   
    alphabet = get_base('lower')
    try:
        infile = open(dictionary_file, 'r',encoding=" ISO-8859-15") 
        dict_words = infile.readlines()
        dict_list = [[] for _ in range(26)]
        for w in dict_words:
            word = w.strip('\n')
            dict_list[alphabet.index(word[0])]+=[word]
        infile.close()
    except FileNotFoundError:
        print('Error(load_hack_dictionary): failed to open given file')
        dict_list = []
    return dict_list
'______________________________________________________________________________'

def is_english(text, hack_dict_list, threshold=0.9):
    """
    ----------------------------------------------------
    Parameters:   text (str)
                  hack_dict_list (list): dictionary list
                  threshold (float): number between 0 to 1
                      default value = 0.9
    Return:       True/False
    Description:  Check if a given file is a plaintext
                  If #matches/#words >= threshold --> True
                      otherwise --> False
                  If invalid threshold, set to default value of 0.9
                  An empty text should return False
                  Assumes a valid dictionary_list is passed
    ---------------------------------------------------
    """
    if text == '':
        return False
    
    result = count_matches(text, hack_dict_list)
    percentage = result[0]/(result[0]+result[1])
    
    if type(threshold) != float or threshold < 0 or threshold > 1:
        threshold = 0.9 
    
    if percentage >= threshold:
        return True
    return False
'______________________________________________________________________________'

def count_matches(text, word_list):
    """
    ----------------------------------------------------
    Parameters:   text (str)
                  word_list (list)
    Return:       matches (int)
                  mismatches (int)
    Description:  Reads a given text, checks if each word appears in given word_list
                  Returns number of matches and mismatches.
                  Words are compared in lowercase
                  Assumes word_list is 2D (output of dictionary_to_list)
    Asserts:      text is a string and dict_list is a list
    ---------------------------------------------------
    """
    assert type(text) == str and type(word_list) == list, 'invalid input'
    words = text_to_words(text)
    alphabet = get_base('lower')
    matches = 0
    mismatch = 0
    for w in words:
        if w.isalpha():
            list_num = alphabet.index(w[0].lower())
            if w.lower() in word_list[list_num]:
                matches+=1
            else:
                mismatch+=1
        else:
            mismatch+=1
    return matches,mismatch
'______________________________________________________________________________'

def text_to_words(text):
    """
    ----------------------------------------------------
    Parameters:   text (str)
    Return:       word_list (list)
    Description:  Reads a given text
                  Returns a list of strings, each pertaining to a word in the text
                  Words are separated by a white space (space, tab or newline)
                  Gets rid of all special characters at the start and at the end
    Asserts:      text is a string
    ---------------------------------------------------
    """
    assert type(text) == str, 'invalid input'
    special = get_base('special')
    word_list = []
    lines = text.split('\n')
    for line in lines:
        line = line.strip('\n')
        line = line.split(' ')
        for i in range(len(line)):
            if line[i] != '':
                line[i] = line[i].strip(special)
                word_list+=[line[i]]
    return word_list
'______________________________________________________________________________'

def file_to_text(filename):
    """
    ----------------------------------------------------
    Parameters:   filename (str)
    Return:       contents (str)
    Description:  Utility function to read contents of a file
                  Can be used to read plaintext or ciphertext
    Asserts:      filename is a valid name
    ---------------------------------------------------
    """
    assert is_valid_filename(filename), 'invalid filename'
    infile = open(filename,'r')
    contents = infile.read()
    infile.close()
    return contents

'______________________________________________________________________________'

def text_to_file(text, filename):
    """
    ----------------------------------------------------
    Parameters:   text (str)
                  filename (str)            
    Return:       no returns
    Description:  Utility function to write any given text to a file
                  If file already exist, previous contents will be erased
    Asserts:      text is a string and filename is a valid filename
    ---------------------------------------------------
    """
    assert type(text) == str , 'invalid text'
    assert is_valid_filename(filename), 'invalid filename'
    outfile = open(filename,'w')
    outfile.write(text)
    outfile.close()
    return
'______________________________________________________________________________'
def is_valid_filename(filename):
    """
    ----------------------------------------------------
    Parameters:   filename (str)
    Return:       True/False
    Description:  Checks if given input is a valid filename 
                  a filename should have at least 3 characters
                  and contains a single dot that is not the first or last character
    ---------------------------------------------------
    """
    if type(filename) != str:
        return False
    if len(filename) < 3:
        return False
    if '.' not in filename:
        return False
    if filename[0] == '.' or filename[-1] == '.':
        return False
    if filename.count('.') != 1:
        return False
    return True

'______________________________________________________________________________'
def get_char_indexes(text,base):
    """
    ----------------------------------------------------
    Parameters:   text (str): input string
                  base (str):  stream of unique characters
    Return:       char_indexes (2D list)
    Description:  Analyzes a given text for any occurrence of base characters
                  Returns a 2D list with characters and their respective indexes
                  format: [[char1,index1], [char2,index2],...]
                  Example: get_char_indexes('I have 3 cents.','c.h') -->
                      [['h',2],['c',9],['.',14]]
                  items are ordered based on their occurrence in the text
    Asserts:      text and base are strings
    ---------------------------------------------------
    """
    assert type(text) == str and type(base) == str, 'invalid input'
    positions = []
    for i in range(len(text)):
        if text[i] in base:
            positions.append([text[i],i])
    return positions

'______________________________________________________________________________'

def remove_chars(text,base):
    """
    ----------------------------------------------------
    Parameters:   text (str)
                  base (str)
    Return:       updated_text (str)
    Description:  Constructs and returns a new text which has
                  all characters in original text after removing base characters
    Asserts:      text and base are strings
    ---------------------------------------------------
    """
    assert type(text) == str and type(base) == str, 'invalid input'
    updated_text = ''
    for char in text:
        if char not in base:
            updated_text += char
    return updated_text

'______________________________________________________________________________'

def restore_text(text, char_indexes):
    """
    ----------------------------------------------------
    Parameters:   text (str)
                  char_indexes (list): [[char1,index1],[char2,index2],...]]
    Return:       updated_text (str)
    Description:  Inserts all characters in the char_indexes 2D list (generated by get_char_indexes)
                  into their respective locations
                  Assumes a valid char_indexes 2d list is given
    Asserts:      text is a string and char_indexes is a list
    ---------------------------------------------------
    """
    assert type(text) == str and type(char_indexes) == list, 'invalid input'
    updated_text = text
    for item in char_indexes:
        updated_text = updated_text[:item[1]]+ item[0] + updated_text[item[1]:]
    return updated_text

'______________________________________________________________________________'

def shift_str(s,n,d='l'):
    """
    ----------------------------------------------------
    Parameters:   text (string): input string
                  shifts (int): number of shifts
                  direction (str): 'l' or 'r'
    Return:       update_text (str)
    Description:  Shift a given string by given number of shifts (circular shift)
                  If shifts is a negative value, direction is changed
                  If no direction is given or if it is not 'l' or 'r' set to 'l'
    Asserts:      text is a string and shifts is an integer
    ---------------------------------------------------
    """
    assert type(s) == str and type(n) == int
    if d != 'r' and d!= 'l':
        d = 'l'
    if n < 0:
        n = n*-1
        d = 'l' if d == 'r' else 'r'
    n = n%len(s)
    if s == '' or n == 0:
        return s

    s = s[n:]+s[:n] if d == 'l' else s[-1*n:] + s[:-1*n]
    return s

class Modular:
    """
    ----------------------------------------------------
    Description: Some utility functions for modular arithmetic
    ----------------------------------------------------
    """
    
    @staticmethod
    def gcd(a,b):
        """
        ----------------------------------------------------
        Static Method
        Parameters:   a (int): an arbitrary integer
                      b (int): an arbitrary integer
        Return:       result (int): gcd(a,b)
        Description:  Computes and returns the greatest common divider using
                      the standard Eculidean Algorithm.
                      The implementation can be iterative or recursive
        Errors:       if a or b are non positive integers, return:
                        'Error(MOD.gcd): invalid input'
        ---------------------------------------------------
        """
        if not isinstance(a,int) or not isinstance(b,int) or b == 0 or a == 0:
            return 'Error(MOD.gcd): invalid input'
        if a < 0 or b < 0:
            return Modular.gcd(abs(a),abs(b))
        if b > a:
            return Modular.gcd(b,a)
        if a % b == 0:
            return b
        return Modular.gcd(b, a%b)

    @staticmethod
    def EEA(a,b):
        """
        ----------------------------------------------------
        Static Method
        Parameters:   a (int): an arbitrary integer
                      b (int): an arbitrary integer
        Return:       result (list): [gcd(a,b), s, t]
        Description:  Uses Extended Euclidean Algorithm to find:
                        gcd(a,b) and <s> and <t> such that:
                        as + bt = gcd(a,b), i.e., Bezout's identity
        Errors:       if a or b are 0 or non-integers
                        'Error(MOD.EEA): invalid input'
        ---------------------------------------------------
        """
        if type(a) != int or type(b) != int or a == 0 or b == 0:
            return 'Error(MOD.EEA): invalid input'
        u = [abs(a), 1, 0]
        v = [abs(b), 0, 1]
        r = [0,0,0]
        while v[0] != 0:
            q = u[0]//v[0]
            r = [u[0] - q*v[0], u[1]-q*v[1], u[2]-q*v[2]]
            u = v
            v = r
        return u

    @staticmethod
    def mul_inverse(a,m):
        """
        ----------------------------------------------------
        Parameters:   a (int): an arbitrary positive integer
                      m (int): an arbitrary positive integer
        Return:       mul_inv (int or 'NA')
        Description:  Computes and returns the multiplicative inverse of 
                        current of a mod m
                      if it does not exist returns 'NA'
        Errors:       if a is not a positive integer, or
                      m is not an integer > 1 --> 
                      return 'Error(MOD.get_mult_inv): invalid input'
        ---------------------------------------------------
        """
        if type(a) != int or a <= 0:
            return 'Error(MOD.get_mult_inv): invalid input'
        if type(m) != int or m <= 1:
            return 'Error(MOD.get_mult_inv): invalid input'
        mul_v = 'NA'
        a = a % m
        if a!= 0 and Modular.gcd(a,m) == 1:
            _,s,_ = Modular.EEA(a,m)
            mul_v = s%m
        return mul_v