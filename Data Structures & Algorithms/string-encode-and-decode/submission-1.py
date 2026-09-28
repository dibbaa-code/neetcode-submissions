# algo to 
# encode a list of strings -> encoded string -> network -> decoded to original list of strings

# basically need to write 2 functions encode, decode


class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for str in strs:
            encoded_str +=  f"{len(str)}#{str}"
        return encoded_str # 5#Hello5#World


    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        index = 0
        while index < len(s): # 0 < 14
            length_str = "" 
            while s[index] != "#": 
                length_str += s[index] #5
                index += 1
            length = int(length_str)
            index += 1 
            curr_str = ""
            end_index_curr_str = index + length
            while index < end_index_curr_str:
                curr_str += s[index]
                index += 1
            
            decoded_strs.append(curr_str)
        
        return decoded_strs
            

