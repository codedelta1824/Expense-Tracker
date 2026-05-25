from Engine import ExpenseEngine
from GUI import ExpenseTrackerApp as App

def main():
    print("[System] Initializing Core Business Logic Engine...")
    engine = ExpenseEngine()
    
    print("[System] Bootstrapping Modernized Dashboard Subsystem...")
    # Inject the loaded engine into the UI wrapper
    application = App(engine)
    
    print("[System] GUI loop started successfully.")
    application.mainloop()

if __name__ == "__main__":
    main()