from collections import defaultdict
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_count = defaultdict(int)
        def decryptEmail(email: str) -> str:
            res = ""
            for i in range(len(email)):
                if email[i] == '+':
                    local_name = res[0:i]
                    while email[i] != '@':
                        i+=1
                    domain_name = email[i:len(email)]
                    res += domain_name
                    break
                elif email[i] == '.':
                    continue
                else:
                    res += email[i]
            return res
        for email in emails:
            decrypted_email = decryptEmail(email)
            print (decrypted_email)
            email_count[decrypted_email] += 1
        
        return len(email_count.keys())


