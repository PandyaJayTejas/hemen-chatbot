print("=" * 40)
print("""  HEMEN — AT YOUR SERVICE
  JUST PLUG IN FOR A QUICK CHAT
  TYPE 'exit' TO PULL THE PLUG""")
print("=" * 40)

responses = {
    "hello": "BY THE POWER OF GRAYSKULL! A new warrior enters. State your purpose!",
    "who are you": "I am HEMEN, champion of Eternia! Some call me Prince Adam... but you may call me UNSTOPPABLE.",
    "how are you": "I have the power! So yeah, pretty good. You?",
    "who is skeletor": "A bumbling villain with a skull face and big ambitions. Honestly embarrassing at this point.",
    "what is grayskull": "Castle Grayskull is the source of my power. Also great for dramatic transformations.",
    "what is eternia": "My home planet. Beautiful place. Constant attempted takeovers. You know how it is.",
    "who is battle cat": "My tiger. Rides into battle. Zero complaints. Best companion in Eternia.",
    "give me advice": "Face your enemies head on. Also never trust anyone with a skeleton for a face.",
    "help": "Ask me about Eternia, Skeletor, my power, or just say hello warrior!",
}

while True:
    user_input = input("You: ")
    clean = user_input.lower().strip()
    if clean in ("exit", "quit", "bye"):
        print("HEMEN: Goodbye! Have a great day!")
        break
    reply = responses.get(clean, "I don't understand that, warrior. Try 'help'.")
    print(f"HEMEN: {reply}") 