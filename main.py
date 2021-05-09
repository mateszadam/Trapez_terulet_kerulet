def main() -> None:
    print('Trapéz kerület és terüet számolás!')
    A: float = float(input('a: '))
    B: float = float(input('b: '))
    C: float = float(input('c: '))
    D: float = float(input('d: '))
    M: float = float(input('m: '))
    Terület: float = 0
    Kerület: float = 0
    if A <= 0 or B <= 0 or C <= 0 or D <= 0 or M <= 0:
        print("Nullával és annál kisebb számmal nem lehet számolni")
    else:
        Terület = ((A + B) * M) / 2
        Kerület = A + B + C + D
        print(f'A trapéz területe: {Terület} és a kerülete {Kerület}')


if __name__ == "__main__":
    main()
