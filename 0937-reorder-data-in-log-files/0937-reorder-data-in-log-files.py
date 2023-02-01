class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            splitted = log.split()
            if splitted[1].isnumeric():
                digit_logs.append(splitted)
            else:
                letter_logs.append(splitted)
                
        letter_logs.sort(key=lambda k: (k[1:], k[0]))
        return map(lambda k:" ".join(k), letter_logs + digit_logs)
        
        