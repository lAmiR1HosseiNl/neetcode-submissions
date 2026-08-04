class Solution:
    @staticmethod
    def numUniqueEmails(emails: list[str]) -> int:
        result = set()
        for item in emails:
            email = item.split("@")
            local_name = ''
            host_name = email[1]
            for word in email[0]:
                if word == '.':
                    pass
                elif word == '+':
                    break
                else:
                    local_name += word

            result.add(local_name+ host_name)
        
        return len(result)