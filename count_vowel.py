def vowel():
    str="We are going to calculate the no of vowels."
    vow="aeiouAEIOU"

    count=0;
    for character in str:
        if character in vow:
            count+=1
            print(character)

    print("No. of vowels in string: ",count)

vowel();
