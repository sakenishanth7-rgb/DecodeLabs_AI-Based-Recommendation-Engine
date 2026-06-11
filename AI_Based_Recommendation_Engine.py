# AI Recommendation Logic

items = {
    "Python Course": ["python", "programming"],
    "Machine Learning Course": ["python", "ai", "machine learning"],
    "Data Science Course": ["python", "data science", "analytics"],
    "Web Development Course": ["html", "css", "javascript"],
    "Deep Learning Course": ["ai", "machine learning", "python"],
    "Computer Vision Course": ["ai", "python", "computer vision"],
    "Natural Language Processing": ["ai", "nlp", "python"],
    "Generative AI Fundamentals": ["ai", "llm", "machine learning"],
    "Cloud Computing": ["aws", "cloud", "devops"],
    "Cyber Security Basics": ["security", "networking", "ethical hacking"],
    "Database Management": ["sql", "database", "data"],
    "Java Programming": ["java", "programming"],
    "C++ Programming": ["c++", "programming"],
    "Android App Development": ["java", "android", "mobile development"],
    "Data Visualization": ["python", "data science", "visualization"],
    "Big Data Analytics": ["hadoop", "spark", "data science"],
    "DevOps Engineering": ["devops", "docker", "kubernetes"],
    "UI/UX Design": ["design", "figma", "user experience"],
    "Blockchain Basics": ["blockchain", "cryptography"],
    "Internet of Things (IoT)": ["iot", "embedded systems", "electronics"],
    "Robotics Fundamentals": ["robotics", "ai", "electronics"],
    "Game Development": ["unity", "c#", "game design"],
    "Software Testing": ["testing", "qa", "automation"],
    "Linux Administration": ["linux", "system administration"],
    "Networking Essentials": ["networking", "security", "infrastructure"]
}

print("=== AI Recommendation System ===")

user_input = input(
    "Enter your interests (comma separated): "
).lower()

user_preferences = [
    interest.strip()
    for interest in user_input.split(",")
]

recommendations = []

for item, tags in items.items():

    similarity_score = len(
        set(user_preferences) & set(tags)
    )

    if similarity_score > 0:
        recommendations.append(
            (item, similarity_score)
        )

recommendations.sort(
    key=lambda x: x[1],
    reverse=True
)

print("\nRecommended Items:")

if recommendations:
    for item, score in recommendations:
        print(f"- {item} (Match Score: {score})")
else:
    print("No recommendations found.")
