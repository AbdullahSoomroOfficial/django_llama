from django.http import JsonResponse
from ollama import chat
from ollama import ChatResponse

from django.shortcuts import render

# conversation_history = [
#     {"role": "user", "content": '"I am from hyderabad"'},
#     {
#         "role": "assistant",
#         "content": "Hyderabad is a great city!\n\nAre you referring to Hyderabad, India? Or maybe the one in Pakistan?\n\nEither way, what's your connection to the city? Are you born and raised there, or did you move there for work or education?",
#     },
#     {"role": "user", "content": '"Hyderabad in Pakaistan. I born here."'},
#     {
#         "role": "assistant",
#         "content": "So you're from Hyderabad, Pakistan!\n\nThat's a beautiful city with a rich history and culture. What's it like growing up in Hyderabad?\n\nDo you have a favorite spot in the city or a favorite dish that reminds you of your hometown?",
#     },
#     {"role": "user", "content": '"My name is Abdullah"'},
#     {
#         "role": "assistant",
#         "content": "Nice to meet you, Abdullah! You're from Hyderabad, Pakistan, and you were born there.\n\nWhat do you like to do for fun, Abdullah? Do you have any hobbies or interests that bring you joy?\n\nAnd what about your family? Do you have siblings, or are you an only child?",
#     },
#     {"role": "user", "content": '"I like coding"'},
#     {
#         "role": "assistant",
#         "content": "That's awesome, Abdullah! Coding is a great hobby and skill to have!\n\nWhat kind of coding do you enjoy the most? Is it web development, mobile app development, or something else?\n\nDo you have any favorite programming languages or frameworks that you're interested in?\n\nAnd what motivates you to keep learning and improving your coding skills?",
#     },
#     {"role": "user", "content": '"I love javascript"'},
#     {
#         "role": "assistant",
#         "content": "A JavaScript enthusiast!\n\nThat's a great choice, Abdullah! JavaScript is an incredible language with so many possibilities. What is it about JavaScript that you love the most?\n\nAre you interested in building web applications, creating interactive experiences, or maybe even developing desktop or mobile apps with Node.js?\n\nHave you worked on any personal projects or contributed to open-source projects using JavaScript?",
#     },
#     {"role": "user", "content": '"Its is lingua franca"'},
#     {
#         "role": "assistant",
#         "content": "You're saying that JavaScript is like the \"lingua franca\" of programming languages!\n\nThat's a great point, Abdullah! JavaScript has become so ubiquitous and widely used that it's often the go-to language for many web development tasks.\n\nWhether you're building a simple web page or a complex enterprise application, JavaScript is likely to be involved in some way. And with its popularity comes a vast array of libraries, frameworks, and tools to help you build amazing things!\n\nWhat do you think makes JavaScript so well-suited as a lingua franca? Is it its ease of use, its flexibility, or something else entirely?\n\nKeep sharing your thoughts, Abdullah!",
#     },
# ]

# def chat_completions(request):
#     user_input = request.GET.get("prompt", "")
#     if not user_input:
#         return JsonResponse({"error": "No input provided."}, status=400)
#     conversation_history.append({"role": "user", "content": user_input})
#     try:
#         response = ollama.chat(model="llama3", messages=conversation_history)
#         prompt_response = response["message"]["content"]
#         conversation_history.append({"role": "assistant", "content": prompt_response})
#         print(conversation_history)
#         return JsonResponse({"response": prompt_response})
#     except Exception as e:
#         return JsonResponse({"error": str(e)}, status=500)


def chat_view(request):
    return render(request, "django_llama_api/chat.html")


conversation_history = [
    {
        "role": "system",
        "content": "You are a helpful assistant. Keep answers short and relevant.",
    },
]


def chat_completions(request):
    user_input = request.GET.get("prompt", "")
    if not user_input:
        return JsonResponse({"error": "No input provided."}, status=400)

    # Add user input to the conversation history
    conversation_history.append(
        {"role": "user", "content": user_input + " (Keep it short.)"}
    )

    # Keep only the last 4-6 interactions, excluding the system message
    max_history_length = 12  # 6 interactions = 12 messages (user + assistant)
    truncated_history = [conversation_history[0]] + conversation_history[-12:]

    try:
        # Call the model with the truncated history
        response: ChatResponse = chat(
            model="llama3",
            messages=truncated_history,
            options={"max_tokens": 50},
        )
        prompt_response = response["message"]["content"]

        # Append the assistant's response to the conversation history
        conversation_history.append({"role": "assistant", "content": prompt_response})

        # Return the response
        return JsonResponse({"response": prompt_response})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
