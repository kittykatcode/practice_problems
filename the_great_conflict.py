#The Evil King of Numbers wants to conquer all space in the Digital World. For that reason, His Evilness declared war on Letters, which actually stay in the Alphabet Fragmentation. You were nominated the Great Arbiter and must provide results of battles to the technology God 3 in 1, Llib Setag-Kram Grebrekcuz-Nole Ksum.
#
#Description
#armyLetters consists of letters from 'a' to 'z' and armyNumbers consists of digits from '1' to '9'. The power of a letter is its position in the Latin alphabet, so the letter 'a' has power 1, 'b' has 2, .. 'z' has 26. The power of a digit is its value, so '1' has power 1, '2' has 2, .. '9' has 9.
#
#armyLetters fights from its end; armyNumbers fights from its beginning.
#
#Per round, one letter from armyLetters attacks one digit and does damage equal to its power, and one digit from armyNumbers attacks two letters and does damage equal to its power to both. Characters with 0 or lower power disappear.
#
#Rounds of battle continue until at least one army has completely disappeared.
#
#Output
#If either or both armies are empty at the start of hostilities, return "Peace".
#At the end of the war, return "Draw" if both armies died, or the final state of the winning army (as a String).
#


import string

def battle_codes(chars,nums):
    print(chars,nums)
    if not chars or not nums: return 'Peace'
    
    chars,nums = [ord(c)-96 for c in chars], [*map(int,nums[::-1])]
    
    while chars and nums:
        c,n = chars[-1], nums[-1]
        chars[-1], nums[-1] = c-n, n-c
        if len(chars)>1: chars[-2] -= n
        
        if nums[-1]<1:                   nums.pop()
        if len(chars)>1 and chars[-2]<1: chars.pop(-2)
        if chars[-1]<1:                  chars.pop()
    
    
    if not chars and not nums: return 'Draw'
    return ''.join( chars and (chr(c+96) for c in chars) or map(str,nums[::-1]) ) 

print(battle_codes(('abc', "12")))