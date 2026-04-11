class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. identify which strings are anagrams.
        #   1.a pull strings from each character into a array/set
        #   1.b check whether the lengths of each string are equal, 
            # can either sort each string, 
            # and or build a hashmap that checks for repeated chars and checks if they're equal
            # if equal, group them then check that the characters are the same 
        # 2. sort the anagrams to be grouped together
        
        # should I build an hashmap for each string
        # how do I group repeated strings together keeping them in order
        # num & set of strings == word == another num # set of strings

        """
        Inputs: strs: array of strings
        Outputs: grouped anagrams into a sublist
        """
        seenStrs = {}

        # Goal: build a dictionary that sorts the characters in the words,
        # Then adds to a dictionary that groups them into
        # {key(word) : value(grouped sorted anagrams)

        for word in strs:
            # If their sorted words are equal, then they are anagrams
            fingerprint = sorted(word) # sorts the letters of the word
            t_fingerprint = tuple(fingerprint) # Dict does not accept list

            if t_fingerprint not in seenStrs: # If not seen before --> create new list list
                seenStrs[t_fingerprint] = [word]
            else:
                # If it is seen again, append it to word
                if t_fingerprint in seenStrs:
                    seenStrs[t_fingerprint].append(word)

        return list(seenStrs.values())