c = {
    "notebook": 4.50,
    "pen": 1.25,
    "stapler": 6.99,
    "envelope_pack": 3.75
}
total = sum(c.values())
print("Items:", ", ".join(c.keys()))
print("Total bill:", total)
