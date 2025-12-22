import re

def analizar_expresion(expresion: str):
    expr = expresion.replace(' ', '')

    vars_found = sorted({c.lower() for c in expr if c.isalpha()})

    ops_explicitas = len(re.findall(r'[+\-*]', expr))
    implicit_digit_letter = len(re.findall(r'(?=\d+[A-Za-z])', expr))
    implicit_letter_letter = len(re.findall(r'(?=[A-Za-z]{2})', expr))
    implicit_before_paren = len(re.findall(r'(?=[A-Za-z0-9]\()', expr))
    implicit_paren_after = len(re.findall(r'(?=\)[A-Za-z(])', expr))

    total = (
        ops_explicitas
        + implicit_digit_letter
        + implicit_letter_letter
        + implicit_before_paren
        + implicit_paren_after
    )

    return {
        'variables': vars_found,
        'num_variables': len(vars_found),
        'total_operaciones': total
    }

if __name__ == '__main__':
    entrada = input('Ingrese la función matemática: ')
    resultado = analizar_expresion(entrada)
    print(resultado)
