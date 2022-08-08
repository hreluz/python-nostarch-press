favorite_languages = {
    'jen': 'Python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favourite language is {language}.")

print("\nUsing get() to Access Values")
alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)