T = int(input())
subject = ["Algorithm", "DataAnalysis", "ArtificialIntelligence", "CyberSecurity", "Network", "Startup", "TestStrategy"]
number = [204, 207, 302, "B101", 303, 501, 105]
for i in range(T):
    string = input()
    print(number[subject.index(string)])