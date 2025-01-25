speeds = [48, 47, 54, 50, 42, 68, 39, 46]

print("Recorded values:", ", ".join(map(str, speeds)))

speeding_vehicles = list(filter(lambda speed: speed > 50, speeds))
print("Speed too high:", ", ".join(map(str, speeding_vehicles)))

