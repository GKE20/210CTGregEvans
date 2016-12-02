//Pseudocode

VOWELS = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U") //The array of vowels
                                                            //in lower case and
                                                            //capitals

word = raw input("")    //Input from the user, with the word they want to remove
                        //the vowels from

new word = ""   //This variable will be the return value in the end with
//just the consonants remaining with all vowels removed from the original input

for letter <- word             //For loop to check if
                                //each letter is not in the vowels
    if letter not <- VOWELS     
       new word += letter       //This part then returns the new word with 
                                //what is already in it plus each of the letters
                                //that is not in the vowels

output(new word)
