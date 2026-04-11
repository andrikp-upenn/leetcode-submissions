class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
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

#Hashmap solution: 25/25 test cases @ 8.0MB, 37ms
