class Solution:
    """
    Goal: Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

    Constraints:
    0 <= strs.length < 100
    0 <= strs[i].length < 200
    strs[i] contains any possible characters out of 256 valid ASCII characters.
    """

    def encode(self, strs: List[str]) -> str:
        new_str = ''
        for word in strs:
            new_str += f'{len(word)}#'+ word
        return new_str


    def decode(self, s: str) -> List[str]:
         # 1. Need to find the # in the strings,
         # 2. Decode the str by slicing it by len(str)
         # 3. Build the str back up
        i = 0
        result = []
        while i < len(s):
            idx = s.index('#', i) # finds '#' from pos i
            len_str = int(s[i:idx]) # Number between current_pos and '#'
            word = s[idx + 1: idx + 1 + len_str] # Word start at idx+1 --> idx+1+len_str
            result.append(word)
            i = int(idx+1+len_str) # update i to start in new word

        return result

