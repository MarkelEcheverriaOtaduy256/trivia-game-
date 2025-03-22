import random
import json

# Cargar el dataset de preguntas desde un archivo JSON
with open(r'c:\Users\marke\OneDrive\Documentos\IA\Python\trivia.json', 'r', encoding='utf-8') as f:
    trivia_data = json.load(f)

# Función para evaluar la respuesta del usuario
def evaluate_answer(user_input, correct_answer):
    if user_input.lower() == correct_answer.lower():
        return "correcta"
    else:
        return "incorrecta"

# Función principal del juego de trivia
def trivia_game():
    print("¡Bienvenido al Trivial Jedi! Te haré preguntas de cultura general de cualquier categoría. Escribe 'salir' para terminar.")
    score = 0
    total_questions = 0
    print("Para cada pregunta, escribe tu respuesta. ¡Buena suerte!")
    
    while True:
        category = random.choice(trivia_data['categories'])
        item = random.choice(category['questions'])
        question = item['question']
        correct_answer = item['answer'].lower()
        
        print(f"Pregunta: {question}")
        user_input = input("Tu respuesta: ").strip().lower()
        
        if user_input == 'salir':
            break
        
        total_questions += 1
        result = evaluate_answer(user_input, correct_answer)
        
        if result == correct_answer:
            print(f"¡Correcto! La respuesta es: {correct_answer}")
            score += 1
        else:
            print(f"Incorrecto. La respuesta correcta era: {correct_answer}")
        
        print(f"Puntuación: {score}/{total_questions}\n")

    print(f"Juego terminado. Puntuación final: {score}/{total_questions}")

# Ejecutar el juego
if __name__ == "__main__":
    trivia_game()
