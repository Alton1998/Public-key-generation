import numpy as np
from random import randint

# Class to implement a novel approach with Matrix
# based Public key Crypto Systems
class PublicKeyCrypto:

    # Function to genrate generator matrix
    def __generate_matrix(self,low=100000000,high=10000000000000000,size=500):
        matrix = np.random.randint(low,high,size=(size,size))
        return matrix
    
    def __genrate_start_point(self,low,high):
        start_point = randint(low,high)
        return start_point
    
    # Function to generate the field
    def __select_field(self,low=1000000,high=10000000000000000):
        field = randint(low,high)
        return field
        
    # Function to generate
    def __generate_private_key(self,low=10000000000,high=1000000000000000000):
        private_key  = randint(low,high)
        return private_key

    # Generate the public key
    def __generate_public_key(self,matrix,low=1000000000,high=10000000000000000000,private_key=0,field=0):
        public_key = np.linalg.matrix_power(matrix,private_key)
        public_key = public_key % field
        return public_key
    
    # Generate random number
    def __generate_random_number(self,low=10000000,high=1000000000000000000000):
        random_no = randint(low,high)
        return random_no

    #  Returns an array with alphabets [a,b,c,...]
    def __init_alpha(self):
        alpha = 'a'
        alpha_list = list()
        for i in range(0,26):
            alpha_list.append(alpha)
            alpha = chr(ord(alpha)+1)
        return alpha_list
    
    # Convert plain text to lisy
    def __convert_to_list(self,plain_text):
        plain_text = plain_text.lower()
        plain_text = plain_text.replace(" ","")
        plain_text = list(plain_text)
        return plain_text

    # Returns alphanumeric value
    def ___convert_to_alphanumeric(self,plain_text = ""):
        alpha_list = self.__init_alpha()
        plain_text = self.__convert_to_list(plain_text)
        new_plain_text = list()
        for i in plain_text:
            new_plain_text.append(alpha_list.index(i))
        return new_plain_text
    
    # Returns alphabet
    def __convert_to_alpha(self,plain_text):
        alpha_list = self.__init_alpha()
        new_plain_text = list()
        for i in plain_text:
            new_plain_text.append(alpha_list[i])
        return new_plain_text
    
    # multiplies public key n times
    def __power_public_key(self,public_key,random_no):
        powered_public_key = np.linalg.matrix_power(public_key,random_no)
        return powered_public_key
    
    # Returns plain text matrix
    def __generate_plain_text_matrix(self,shape,plain_text,start_point):
        plain_text_matrix = np.random.randint(1,100,size=(shape[0],shape[1]))
        plain_text_matrix = np.reshape(plain_text_matrix,(1,shape[1]*shape[0]))

        for i in range(0,len(plain_text)):
            plain_text_matrix[0][start_point] = plain_text[i]
            start_point = start_point + 1
        
        plain_text_matrix = np.reshape(plain_text_matrix,shape)

        return plain_text_matrix
    
    # writes array to file
    def __write_to_file(self,name,text):
        np.save(name,text)
    
    # writes array to file .txt
    def __write_to_file_txt(self,name,text):
        np.savetxt(name,text,fmt="%s")

    # Performs encryption
    def encrypt(self,plain_text=""):
        if not plain_text.strip():
            raise Exception("Text is empty")
        else:
            plain_text = self.___convert_to_alphanumeric(plain_text=plain_text)
            g = self.__generate_matrix()
            r = self .__generate_random_number()
            shape_matrix = g.shape
            start_point = self.__genrate_start_point(low=1,high=shape_matrix[0]*shape_matrix[1])
            private_key = self.__generate_private_key()
            field = self.__select_field()
            public_key = self.__generate_public_key(matrix=g,private_key=private_key,field=field)
            powered_public_key = self.__power_public_key(public_key,r)
            c2 = public_key
            self.__write_to_file("cipher2",c2)
            start_point = start_point-len(plain_text)-1
            plain_text_matrix = self.__generate_plain_text_matrix(g.shape,plain_text,start_point)
            c1 = np.add(plain_text_matrix,powered_public_key)%26
            self.__write_to_file("cipher1",c1)
            key1 = start_point*r
            key2 = start_point*len(plain_text)
            keys = list()
            keys.append(r)
            keys.append(key1)
            keys.append(key2)
            self.__write_to_file("key",keys)

    # performs decryption
    def decrypt(self,c1="cipher1.npy",c2="cipher2.npy",keys = "key.npy"):
        c1 = np.load(c1,allow_pickle=True)
        self.__write_to_file_txt("cipher1.txt",c1)
        c2 = np.load(c2,allow_pickle=True)
        self.__write_to_file_txt("cipher2.txt",c2)
        keys = np.load(keys,allow_pickle=True)
        r,key1,key2 = keys
        c2 = np.linalg.matrix_power(c2,r)
        plain_text=np.subtract(c1,c2)%26
        shape = plain_text.shape
        plain_text = np.reshape(plain_text,(1,shape[0]*shape[1]))
        plain_text = plain_text[0]
        plain_text = self.__convert_to_alpha(plain_text)
        start_point = int(key1/r)
        length = int(key2/start_point)
        new_plain_text = list()
        for i in range(0,length):
            new_plain_text.append(plain_text[start_point])
            start_point = start_point + 1
        self.__write_to_file_txt("plain_text.txt",new_plain_text)


if __name__=='__main__':
    p=PublicKeyCrypto()
    p.encrypt(plain_text="hinal")
    p.decrypt()