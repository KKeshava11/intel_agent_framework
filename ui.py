from core.agent import Agent
from flows.sample_flow import sample_flow

def start_ui():
    print("=== Agentic Framework Console ===")
    agent = Agent(name="IntelAgent")

    while True:
        print("\nOptions:")
        print("1. Run sample flow")
        print("2. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            sample_flow(agent)
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid choice")
