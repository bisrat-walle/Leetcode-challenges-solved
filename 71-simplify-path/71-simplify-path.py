class Solution:
    def simplifyPath(self, path: str) -> str:
        file_folder_names = path.split("/")
        stack = []
        for name in file_folder_names:
            if name == "." or name=="":
                continue
            elif name == "..":
                stack.pop() if stack else None
            else:
                stack.append(name)
        simplified_path = "/" + "/".join(stack)
        
        return simplified_path