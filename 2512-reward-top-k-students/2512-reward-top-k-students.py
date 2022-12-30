class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)
        points = defaultdict(int)
        n = len(report)
        for i in range(n):
            fs = report[i].split()
            for f in fs:
                if f in positive_feedback:
                    points[student_id[i]] += 3
                elif f in negative_feedback:
                    points[student_id[i]] -= 1
                else:
                    points[student_id[i]] += 0
        
        arr = []
        for key in points:
            arr.append((-points[key], key))
        arr.sort()
        ans = []
        # print(arr)
        for i in range(k):
            ans.append(arr[i][1])
        # print(arr)
        return ans