"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
    
        def calculateTotalImportance(employee , imp=0):
            if not employee.subordinates:
                return employee.importance
            an = employee.importance
            for emp in employees:
                if emp.id in employee.subordinates:
                    an += calculateTotalImportance(emp)
            
            return an
    
        for employee in employees:
            if employee.id == id:
                emp = employee
                break
        return calculateTotalImportance(emp)
            
            
            