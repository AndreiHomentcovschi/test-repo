import random


def roll_dice(sides: int = 6, count: int = 2) -> list[int]:
    return [random.randint(1, sides) for _ in range(count)]


def fizzbuzz(n: int) -> list[str]:
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    print("Dice roll:", roll_dice())
    print("FizzBuzz:", ", ".join(fizzbuzz(15)))
    print("Primes under 50:", [n for n in range(50) if is_prime(n)])
