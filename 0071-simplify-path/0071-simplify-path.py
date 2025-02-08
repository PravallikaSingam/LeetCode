class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        components = path.split("/")
        
        for component in components:
            if component == "" or component == ".":
                continue  # Ignore empty parts and current directory
            elif component == "..":
                if stack:
                    stack.pop()  # Go back to the parent directory
            else:
                stack.append(component)  # Add valid directory name
        
        return "/" + "/".join(stack)  # Construct the final path

        