# https://leetcode.com/problems/unique-email-addresses/
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        if not emails:
            return 0

        # Or use set()
        emailDict = {}  # key = domain, val = local

        for email in emails:
            local, domain = email.split('@')

            if domain not in emailDict.keys():
                emailDict[domain] = []

            local = ''.join(local.split('.'))

            # if '+' in local:
            #     local = local[0: local.index('+')]
            local = local.split('+')[0]

            if local not in emailDict[domain]:
                emailDict[domain].append(local)

        res = 0

        for key in emailDict.keys():
            res += len(emailDict[key])

        return res



sol = Solution()
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
sol.numUniqueEmails(emails)