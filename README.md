# Validar CPF

Esse script consiste em validar CPF de acordo com o cálculo indicado pelo Ministério da Fazenda.

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte **[Implantação](#-implanta%C3%A7%C3%A3o)** para saber como implantar o projeto.

### 📋 Pré-requisitos

De que coisas você precisa para instalar o software e como instalá-lo?

```
Windows 10 22H2
Python 3.11
```

### 🔧 Implantação


Para o funcionamento correto deve-se instânciar a classe CPF passando como parâmentro o cpf desejado:

```
cpf = CPF('123456789-00')
```

Após a instância parametrizada feita,
utlize o método de validação, o mesmo irá retornar True ou False dependendo se o CPF é válido ou não :
```
cpf.is_valid()
    #False
```



## 🛠️ Construído com

* [Python 3.11](https://www.python.org/downloads/release/python-3110/) - A versão do python utilizado

## ✒️ Autor

* **Matheus Guilherme** - *Developoer* - [MatheusKDev](https://www.instagram.com/matheuskdev)
