import pywinctl

def perform_action(command):
    if command == "CLOSE_APP":
        try:
            active = pywinctl.getActiveWindow()
            active.close()
            print("✅ App closed.")
        except Exception as e:
            print(f"❌ Error: {e}")
    elif command == "CALL_PERSON":
        print("📞 (Simulated) Calling person...")
    elif command == "ANSWER_CALL":
        print("📲 (Simulated) Answering call...")
    else:
        print("❓ Command not recognized.")
