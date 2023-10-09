def kinetic_energy(mass, velocity):
    kinetic_energy = 0.5 * mass * velocity**2
    return kinetic_energy

def main():
    mass = float(input("Enter the mass of the object (in kilograms): "))
    velocity = float(input("Enter the velocity of the object (in meters per second): "))
    ke = kinetic_energy(mass, velocity)
    print(f"Kinetic energy of the object: {ke:.2f} joules")

if __name__ == "__main__":
    main()