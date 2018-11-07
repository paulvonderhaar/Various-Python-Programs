#  File: Spiral.py
 
#  Description: Print 8 numbers around a given number in a spiral
 
#  Student Name: Kyle Katzen
 
#  Student UT EID: kzk66
 
#  Partner Name: Paul Vonder Haar
 
#  Partner UT EID: pmv 347
 
#  Course Name: CS 313E
 
#  Unique Number: 51730
 
#  Date Created: 1/31/15
 
#  Date Last Modified: 1/31/15
 
def substitution_encode ( strng ):
  cipher = [ "q", "a", "z", "w", "s", "x", "e","d","c","r", "f","v","t","g","b","y","h","n","u","j","m","i","k","o","l","p"]
  #Define empty string that we will return as encoded text
  temp_str = ""
  #Go through every letter in the phrase
  for i in range(0,len(strng)):
      #If its a space, simply add it to the encoded text and move to the next character
      if strng[i] == (" "):
        temp_str += " "
      else:
          #Find the position that the letter in the phrase has in the alphabet, and then pick out the right letter from cipher using that index
        temp_str += cipher[ord(strng[i]) - ord("a")]   
  return temp_str
   
def substitution_decode ( strng ):
  cipher = [ "q", "a", "z", "w", "s", "x", "e","d","c","r", "f","v","t","g","b","y","h","n","u","j","m","i","k","o","l","p"]
  temp_str = ""
  #Go through all the letters in the phrase that we are decoding
  for i in range(0,len(strng)):
      #If it is a space, add it and move
      if strng[i] == (" "):
        temp_str += " "
      else:
          #Now we find the location of the sipher, add a to it, and that number corresponds to the ascii code for the decoded letter
        temp_num = cipher.index(strng[i])+ord("a")
        temp_str += chr(temp_num)    
  return temp_str
  ...
 
def vigenere_encode ( strng, passwd ):
  alf = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  temp_str = ""
  temp_pwd = ""
  j=0
  #For every letter in the string to be coded
  for i in range(0,len(strng)):
      #If it is a space, add it and keep going
      if strng[i] == (" "):
        temp_str += " " 
      else:
        #If we reach the end of the password, go back to the beginning of the password
        if j == len(passwd):
          j = 0
        #We will shift the list alf over by the position of the given letter in passwd
        temp_ord = ord(passwd[j]) - ord("a")
        #We then want to make sure it still will be in line with a number, so to stop overflow, we use mod 26 in order to bring it back down
        temp_ord = temp_ord%26
        #Takes the position in the alphabet of the plain text
        temp_charnum = alf.index(strng[i])
        #adds the password number to that and makes sure it is still in range with mod
        temp_charnum += temp_ord
        temp_charnum = temp_charnum%26
        temp_str += alf[temp_charnum]
        j+=1
  return (temp_str)
 
def vigenere_decode ( strng, passwd ):
  alf = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  temp_str = ""
  temp_pwd = ""
  j = 0
  for i in range(0,len(strng)):
      if strng[i] == (" "):
        temp_str += " " 
        temp_pwd += " "
      else:
        if j == len(passwd):
            j = 0
        #takes the index of the password
        temp_pwdind = alf.index(passwd[j])
        #Takes the index of the string to be decoded
        temp_strind = alf.index(strng[i])
        #Subtracts the password index from the string index
        temp_index = temp_strind - temp_pwdind
        #Looks into alph, and gets the appropriate decoded letter
        temp_str += alf[temp_index]
        j += 1
  return (temp_str)
   
   
   
def main():
  # open file for reading
  in_file = open ("cipher.txt", "r")
 
  # print header for substitution cipher
  print ("Substitution Cipher")
  print ()
 
  # read line to be encoded
  line = in_file.readline()
  line = line.strip()
 
  # encode using substitution cipher
  encoded_str = substitution_encode (line)
 
  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Encoded Text: " + encoded_str)
  print ()
 
  # read line to be decoded
  line = in_file.readline()
  line = line.strip()
 
  # decode using substitution cipher
  decoded_str = substitution_decode (line)
 
  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Decoded Plain Text: " + decoded_str)
  print ()
 
  # print header for vigenere cipher
  print ("Vigenere Cipher")
  print ()
 
  # read line to be encoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  passwd = in_file.readline()
  passwd = passwd.strip()
 
  # encode using vigenere cipher
  encoded_str = vigenere_encode (line, passwd)
 
  # print result
  print ("Plain Text to be Encoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Encoded Text: " + encoded_str)
  print ()
 
  # read line to be decoded and pass phrase
  line = in_file.readline()
  line = line.strip()
  passwd = in_file.readline()
  passwd = passwd.strip()
 
  # decode using vigenere cipher
  decoded_str = vigenere_decode (line, passwd)
 
  # print result
  print ("Encoded Text to be Decoded: " + line)
  print ("Pass Phrase (no spaces allowed): " + passwd)
  print ("Decoded Plain Text: " + decoded_str)
  print ()
 
  # close file
  in_file.close()
 
main()