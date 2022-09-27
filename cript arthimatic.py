from ortools.sat.python
import cp_model model = cp_model.CpModel() 
base = 10
c = model.NewIntVar(1, 9, 'C') 
p = model.NewIntVar(0, 9, 'P') 
i = model.NewIntVar(1, 9, 'I') 
s = model.NewIntVar(0, 9, 'S') 
f = model.NewIntVar(1, 9, 'F') 
u = model.NewIntVar(0, 9, 'U') 
n = model.NewIntVar(0, 9, 'N') 
t = model.NewIntVar(1, 9, 'T') 
r = model.NewIntVar(0, 9, 'R') 
e = model.NewIntVar(0, 9, 'E') 
letters = [c, p, i, s, f, u, n, t, r, e] 
model.AddAllDifferent(letters) 
model.Add(c * 10 + p + i * 10 + s + f* base*2 + u * 10 + n == t * 103 + r * 10*2 + u * 10 + e) 
	class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback): 
	def init (self, variables): 
		cp_model.CpSolverSolutionCallback. init (self) 
		self. variables = variables 
		self. solution_count = 0 
	def on_solution_callback(self): 
		self. solution_count += 1 
		for v in self. variables: 
			print(%s=%i , %(v, self.Value(v)), end=" ")
 		print() 
	def solution_count(self):
 		return self. solution_count
solver = cp_model.CpSolver()
solution_printer = VarArraySolutionPrinter(letters)
status = solver.SearchForAllSolutions(model, solution_printer)
