from utilities import file_to_text, get_base

NAME = 'Qutaiba_Albluwi'     #<------- edit this to be your name, should match your file name

class Midterm:
    
    @staticmethod
    def get_first_name():
        first,_ = NAME.split('_')
        return first  
    
    @staticmethod
    def get_last_name():
        _,last = NAME.split('_')
        return last
    
    @staticmethod    
    def get_ID():
        return '012345678'            #<------- edit this with your student ID
    
    @staticmethod
    def get_certification():
        return 'Type the certification'   #<------- edit this string with your honor pledge

    @staticmethod
    def get_task1_solution():
        key = 'quarrelled' #<---------- hard-code your Task 1 key here
        filename = 'plaintext1_' + NAME + '.txt'
        plaintext = file_to_text(filename)
        return key,plaintext
    
    @staticmethod
    def get_task2_solution():
        key = (27, 46, 7, 58)               #<---------- hard-code your Task 2 key here
        filename = 'plaintext2_' + NAME + '.txt'
        plaintext = file_to_text(filename)
        return key,plaintext
    
    @staticmethod
    def get_task3_solution():
        key = ('alphanum', 'm') #<---------- hard-code your Task 3 sub here
        filename = 'plaintext3_' + NAME + '.txt'
        plaintext = file_to_text(filename)
        return key,plaintext    
    
class CT:
    """
    ----------------------------------------------------
    Cipher name: Columnar Transposition Cipher
    Key:         (str) a keyword
    Type:        Transposition Cipher
    Description: Constructs a table from plaintext, 
                 #columns = len(keyword)
                 Rearrange columns based on keyword reverse order
                 Read the text vertically
                 Applies to all characters except special and whitespace characters
    ----------------------------------------------------
    """
    
    DEFAULT_PAD = 'q'
    DEFAULT_KEY = 'zone'
    DICTIONARY = 'engmix.txt'
    
    def __init__(self,key=DEFAULT_KEY,pad=DEFAULT_PAD):
        """
        ----------------------------------------------------
        Parameters:   __key (str): keyword from engmix.txt
                      __pad (str): a character from alpha
        Description:  Columnar Transposition constructor
                      sets __key and __pad
        ---------------------------------------------------
        """
        # your code here
        pass
    
    def get_key(self):
        """
        ----------------------------------------------------
        Parameters:   -
        Return:       key (str)
        Description:  Returns a copy of columnar transposition key
        ---------------------------------------------------
        """
        # your code here
        return None
    
    def set_key(self,key):
        """
        ----------------------------------------------------
        Parameters:   key (str): keyword
        Return:       success: True/False
        Description:  Sets key to given key
                      if invalid key --> set to default key
                      if valid stores the adjusted value
        ---------------------------------------------------
        """ 
        # your code here
        return None

    def __str__(self):
        """
        ----------------------------------------------------
        Parameters:   -
        Return:       output (str)
        Description:  Constructs and returns a string representation of 
                      Columnar Transposition object
                      output format:
                      Columnar Transposition Cipher:
                      key = <key>, pad = <pad>
        ---------------------------------------------------
        """
        # your code here
        return ''
        
    def get_pad(self):
        """
        ----------------------------------------------------
        Parameters:   -
        Return:       pad (str): current padding character
        Description:  Returns a copy of current padding character
        ---------------------------------------------------
        """ 
        # your code here
        return None
    
    def set_pad(self,pad):
        """
        ----------------------------------------------------
        Parameters:   pad (str): a padding character
        Return:       success: True/False
        Description:  Sets pad to given character
                      a pad should be a single alphabetical character
                      if invalid pad, set to default value
        ---------------------------------------------------
        """
        # your code here
        return None
    
    @staticmethod
    def valid_key(key,words):
        """
        ----------------------------------------------------
        Static Method
        Parameters:   key (?): an arbitrary input
                      words (list): list of dictionary words
        Returns:      True/False
        Description:  Check if given input is a valid Columnar Transposition key
                      A valid key is:
                        A string
                        is a word in DICTIONARY
                        Consists of at least 2 unique lower case characters
        ---------------------------------------------------
        """
        # your code here
        return None

    @staticmethod
    def get_words(dictionary_filename,wordsize=None):
        """
        ----------------------------------------------------
        Static Method
        Parameters:   dictionary_filename (str)           
        Return:       words (list)
        Description:  returns a list of words from given dictionary
                      with the given length
                      if wordsize is None return all words in dictionary
        ----------------------------------------------------
        """ 
        # your code here
        return []
    
    @staticmethod
    def adjust_key(key):
        """
        ----------------------------------------------------
        Static Method
        Parameters:   key (str)           
        Return:       adjusted_key (key)
        Description:  Returns key after adjusting it
                      Removes all non-alpha characters
                      Removes all upper case characters
                      Keeps first occurrence of each character and 
                          removes duplicates
        ----------------------------------------------------
        """ 
        # your code here
        return None
            
    @staticmethod
    def key_order(key):
        """
        ----------------------------------------------------
        Static Method
        Parameters:   key (str)           
        Return:       key_order (list)
        Description:  Returns key order
                      Example: mark --> [2,0,3,1]
                      If invalid key --> return []
                      Adjust key before getting order
        ----------------------------------------------------
        """ 
        # your code here
        return None

    def encrypt(self,plaintext):
        """
        ----------------------------------------------------
        Parameters:   plaintext (str)
        Return:       ciphertext (list)
        Description:  Encryption using Columnar Transposition Cipher
                      Does not include whitespaces in encryption
                      Uses padding
        Asserts:      plaintext is a string
        ----------------------------------------------------
        """
        # your code here
        return None

    def decrypt(self,ciphertext):
        """
        ----------------------------------------------------
        Parameters:   ciphertext (str)
        Return:       plaintext (list)
        Description:  Decryption using Columnar Transposition Cipher
        Asserts:      ciphertext is a string
        ----------------------------------------------------
        """
        # your code here
        return None

    @staticmethod
    def cryptanalyze(ciphertext,student_name):
        # your code here
        return None,None

#-------------------- Task 2: Math Cipher ----------------------
class Mathx:
    """
    ----------------------------------------------------
    Cipher name: Mathx
    Key:         (a,b,c,m)
    Type:        Substitution Cipher
    Description: y = (abb - c)x + bc mod m
                 base = B6
                 m = even number > 25
                 Applies only to characters defined in the base
    ----------------------------------------------------
    """
    BASE = get_base('B6')
    DEFAULT_KEY = (1,1,0,26)

    def __init__(self,key=DEFAULT_KEY):
        """
        ----------------------------------------------------
        Parameters:   __key: tuple(int,int,int,int): (a,b,c,m)
        Description:  Mathx constructor
                      sets __key
        ---------------------------------------------------
        """
        # your code here
        pass

    def get_key(self):
        """
        ----------------------------------------------------
        Parameters:   -
        Return:       key (tuple)
        Description:  Returns a copy of the Mathx key
        ---------------------------------------------------
        """
        # your code here
        return None

    def get_base(self):
        """
        ----------------------------------------------------
        Parameters:   -
        Return:       base (str)
        Description:  Returns a copy of the Mathx base
                        which is a subset of BASE
        ---------------------------------------------------
        """
        # your code here
        return None
                
    @staticmethod
    def valid_key(key):
        """
        ----------------------------------------------------
        Static Method
        Parameters:   key (?):
        Returns:      True/False
        Description:  Checks if given key is a valid Mathx key
                      A valid key is a tuple of 4 integers (a,b,c,m)
                      a,b and c can't be negative numbers
                      m is a positive integer > 25 (what is the max?)
        ---------------------------------------------------
        """
        # your code here
        return None

    def set_key(self,key):
        """
        ----------------------------------------------------
        Parameters:   key (tuple): tuple(int,int,int,int)
        Return:       success: True/False
        Description:  Sets Mathx key to given key
                      If given argument is a valid key, set and return True
                      If necessary set a, b and c to residue values
                      if invalid key --> set to default key and return False
        ---------------------------------------------------
        """ 
        # your code here
        return None

    def __str__(self):
        """
        ----------------------------------------------------
        Parameters:   -
        Return:       output (str)
        Description:  Constructs and returns a string representation of 
                      Mathx object. Used for testing
                      output format:
                      Mathx: y = (<a>*<b>^2-c)*x + <b>*<c> mod <m>
        ---------------------------------------------------
        """
        # your code here
        return ''

    def encrypt(self,plaintext):
        """
        ----------------------------------------------------
        Parameters:   plaintext (str)
        Return:       ciphertext (str)
        Description:  Encryption using Mathx cipher
        Asserts:      plaintext is a string
        ---------------------------------------------------
        """
        # your code here
        return None

    def decrypt(self,ciphertext):
        """
        ----------------------------------------------------
        Parameters:   ciphertext (str)
        Return:       plaintext (str)
        Description:  Decryption using Mathx cipher
        Asserts:      ciphertext is a string
        ---------------------------------------------------
        """
        # your code here
        return None             

    def get_type(self):
        """
        ----------------------------------------------------
        Parameters:   -
        Return:       type (str)
        Description:  Inspects current Mathx cipher and return its type
                      Defined types:
                          Illegal,No_Encipherment, Shift, Decimation, Affine
        ---------------------------------------------------
        """
        # your code here
        return None
    
    @staticmethod
    def key_stat(m):
        """
        ----------------------------------------------------
        Static method
        Parameters:   m (int)
        Return:       Percentages (list of 5 floats)
        Description:  Generates all possible Mathx keys for the given m
                      Inspect the keys to check percentage of:
                          f1: Illegal keys
                          f2: no_encipherment keys
                          f3: shift keys
                          f4: decimation keys
                          f5: affine keys
                      Return [f1,f2,f3,f4,f5]
                      Assume a valid value of m is always given
        ---------------------------------------------------
        """
        # your code here
        return None
    
    @staticmethod
    def cryptanalyze(ciphertext):
        """
        ----------------------------------------------------
        Static method
        Parameters:   ciphertext (str)
        Return:       key (tuple)
                      plaintext (str)
        Description:  Cryptanalyzes a given Mathx ciphertext
        ---------------------------------------------------
        """
        # your code here
        return None,None

#-------------------- Task 3: Atberti Cipher --------------------------
class Atberti:
    """
    ----------------------------------------------------
    Cipher name: A mix of Atbash and Atberti Ciphers
    Key:         (base,pointer)
    Type:        Substitution Cipher
    Description: Generates a base and takes its Atbash (reverse)
                 The base is the outer wheel and the Atbash is the inner wheel
                 First character in Outer wheel is aligned with pointer in inner wheel
    ----------------------------------------------------
    """
    #constants
    BASES = ['lower','upper','alpha','lowernum','uppernum','alphanum','B6','BA','pascii']
    DEFAULT_KEY = ('lower','z')
    
    def __init__(self,key=DEFAULT_KEY):
        """
        ----------------------------------------------------
        Parameters:   __key (str,str): base,pointer
        Description:  Atberti Cipher constructor
                      sets __key
        ---------------------------------------------------
        """
        # your code here
        pass
    
    def get_key(self):
        """
        ----------------------------------------------------
        Parameters:   -
        Return:       key(tuple): (str,str)
        Description:  Returns a copy of the Atberti key
        ---------------------------------------------------
        """
        # your code here
        return None
       
    def set_key(self,key):
        """
        ----------------------------------------------------
        Parameters:   key: tuple(str,str)
        Return:       success: True/False
        Description:  Sets Atberti cipher key to given key
                      if invalid key --> set to default key
        ---------------------------------------------------
        """ 
        # your code here
        return None
    
    def __str__(self):
        """
        ----------------------------------------------------
        Parameters:   -
        Return:       output (str)
        Description:  Constructs and returns a string representation of 
                      Atberti object. Used for testing
                      output format:
                      Atberti Cipher (<key>):
                      <out_wheel>
                      <in_wheel>
        ---------------------------------------------------
        """
        # your code here
        return ''
    
    
    @staticmethod
    def valid_key(key):
        """
        ----------------------------------------------------
        Static Method
        Parameters:   key (?):
        Returns:      True/False
        Description:  Checks if given key is a valid Atberti key
                      The key should be a tuple consisting of 2 arguments
                      The first is a string which should be in BASES
                      The second is a single character defined within the retrieved base
        ---------------------------------------------------
        """
        # your code here
        return None
       
    def get_wheels(self):
        """
        ----------------------------------------------------
        Parameters:   -
        Return:       out_wheel (str)
                      in_wheel (str)
        Description:  returns out and in wheels aligned at pointer
        ---------------------------------------------------
        """
        # your code here
        return None,None

    def encrypt(self,plaintext):
        """
        ----------------------------------------------------
        Parameters:   plaintext (str)
        Return:       ciphertext (str)
        Description:  Encryption using Atberti Cipher
        Asserts:      plaintext is a string
        ---------------------------------------------------
        """
        # your code here
        return None
    
    def decrypt(self,ciphertext):
        """
        ----------------------------------------------------
        Parameters:   ciphertext (str)
        Return:       plaintext (str)
        Description:  Decryption using Atberti Cipher
                      Decryption applies only to characters defined in the wheels
        Asserts:      ciphertext is a string
        ---------------------------------------------------
        """
        # your code here
        return None

    @staticmethod
    def cryptanalyze(ciphertext):
        """
        ----------------------------------------------------
        Static method
        Parameters:   ciphertext (string)
        Return:       key,plaintext
        Description:  Cryptanalysis of Atberti Cipher
                      Returns plaintext and key (base,pointer)
        ---------------------------------------------------
        """
        # your code here
        return None
