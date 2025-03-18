"""
File: pokemon.py
Author: Weijian Zhao(David)
Date: 2025-03-11
Class: CS_5001, Spring_2025
Description: 
homework 2:pokemon
"""
import random


class Pokemon:
    def __init__(self, name, attack, defense, max_health):
        """
        Constructor
        :param name: str, the name of the pokemon
        :param attack: int, the attack power of the pokemon
        :param defense: int, the defense power of the pokemon
        :param max_health: int, the maximum health of the pokemon
        """
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(attack, int):
            raise TypeError("attack must be an integer")
        if attack < 0:
            raise ValueError("attack must be greater than zero")
        if not isinstance(defense, int):
            raise TypeError("defense must be an integer")
        if defense < 0:
            raise ValueError("defense must be greater than zero")
        if not isinstance(max_health, int):
            raise TypeError("max_health must be an integer")
        if max_health <= 0:
            raise ValueError("max_health must be greater than zero")
        self.name = name
        self.attack = attack
        self.defense = defense
        self.max_health = max_health
        self.current_health = max_health

    def __str__(self):
        """
        Return the string representation of the pokemon
        :return: str, the string representation of the pokemon
        """
        return f"{self.name} (health: {self.current_health}/{self.max_health})"

    def lose_health(self, amount):
        """
        Reduce the health of the pokemon
        :param amount: int, the amount of health to reduce
        """
        if not isinstance(amount, int):
            raise TypeError("amount must be an integer")
        if amount < 0:
            pass
        else:
            self.current_health -= amount
            if self.current_health < 0:
                self.current_health = 0

    def is_alive(self):
        """
        Check if the pokemon is alive
        :return: bool, True if the pokemon is alive, False otherwise
        """
        return self.current_health > 0

    def revive(self):
        """
        Revive the pokemon
        """
        self.current_health = self.max_health
        print(f"{self.name} has been revived!")

    def attempt_attack(self, other: "Pokemon") -> bool:
        """
        Attempt to attack another pokemon
        :param other: Pokemon, the other pokemon
        :return: bool, True if the attack is successful, False otherwise
        """
        if not isinstance(other, Pokemon):
            raise TypeError("other must be a Pokemon")
        lucky = round(random.uniform(0.7, 1.3), 1)
        damage = round(self.attack * lucky)
        print(f"{self.name} attacks {other.name} for {damage} damage!")
        net_damage = damage - other.defense
        if net_damage > 0:
            other.lose_health(net_damage)
            return True
        else:
            return False


if __name__ == "__main__":
    p1 = Pokemon("Pikachu", 55, 40, 35)
    print(p1)
    p1.lose_health(10)
    print(p1)
    p1.lose_health(100)
    print(p1)
    print(p1.is_alive())
    p1.revive()
    print(p1)
    print(p1.is_alive())
