# Importa o módulo de expressões regulares
import re 

class CPF:
    def __init__(self, cpf: str) -> None:
        self.cpf: str = self._clean_cpf(cpf)
        self.valid: bool = self._validate_cpf()

    # Remove todos os caractéres não numéricos do cpf
    def _clean_cpf(self, cpf: str) -> str:
        return re.sub(r'[^\d]+', '', cpf)

    def _validate_cpf(self) -> bool:
        cpf: str = self.cpf

        
        if len(cpf) != 11:      # O CPF deve ter 11 dígitos após passar pelo regex
            return False
        
        if len(set(cpf)) == 1:  # Verifica se todos os dígitos são iguais (CPF inválido)
            return False

        # Cálculo do primeiro dígito verificador
        soma: int = sum(int(cpf[i]) * (10 - i) for i in range(9))
        resto: int = 11 - (soma % 11)
        if resto == 10 or resto == 11:
            resto = 0
        if resto != int(cpf[9]):
            return False

        # Cálculo do segundo dígito verificador
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        resto = 11 - (soma % 11)
        if resto == 10 or resto == 11:
            resto = 0
        if resto != int(cpf[10]):
            return False

        # Se o CPF passou por todas as validações, é válido
        return True

    def is_valid(self) -> bool: # Retorna True ou False para a instância da classe
        return self.valid
