//Crie dois pacotes baseados nas atribuições de uma empresa e inclua classes neles.
em python 

# pasta da empresa
- empresa
   - __init__.py
   - finanças.py
   - departamento_pessoal.py

# arquivo finanças.py
class Finanças:
	def __init__(self, despesas, receitas):
    	self.despesas = despesas
    	self.receitas = receitas

	def get_saldo(self):
    	return self.receitas - self.despesas

# arquivo departamento_pessoal.py
class DepartamentoPessoal:
	def __init__(self, funcionarios, salarios):
    	self.funcionarios = funcionarios
    	self.salarios = salarios

	def get_custo_total(self):
    	return sum(self.salarios)
