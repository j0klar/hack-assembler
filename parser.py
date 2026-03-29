class Parser:
    """Parses a single .asm-file into A-, C-, and L-commands."""
    
    def __init__(self, file):
        self.line_count = 0
        self.instr = None
        
        with open(file) as stream:
            self.asm = []
            for line in stream.read().split("\n"):
                line = line.split("//")[0].strip()
                if line: 
                    self.asm.append(line)
             
    def more_commands(self):
        return self.line_count < len(self.asm)
        
    def advance(self):
        self.instr = self.asm[self.line_count]
        self.line_count += 1
        
    def command_type(self):
        if self.instr[0] == "@":
            return "A_COMMAND" # @Xxx
        elif self.instr[0] == "(":
            return "L_COMMAND" # (Xxx)
        else:
            return "C_COMMAND" # dest=comp;jump
        
    def symbol(self):
        if self.command_type() == "A_COMMAND":
            return self.instr[1:] # @Xxx
        elif self.command_type() == "L_COMMAND":
            return self.instr[1:-1] # (Xxx)
        
    def dest(self):
        if "=" in self.instr:
            return self.instr.split("=")[0] # dest=Xxx
        return None
        
    def comp(self):
        if "=" in self.instr:
            right = self.instr.split("=")[1]
            if ";" in right:
                return right.split(";")[0] # dest=comp;jump
            return right # dest=comp
        elif ";" in self.instr:
            return self.instr.split(";")[0] # comp;jump
        else:
            return self.instr # comp
        
    def jump(self):
        if ";" in self.instr:
            return self.instr.split(";")[1] # Xxx;jump
        return None
