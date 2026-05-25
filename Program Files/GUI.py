import customtkinter as ctk
from tkinter import ttk
import tkinter.messagebox as messagebox
from datetime import date

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("dark-blue") 

COLOR_BG_PRIMARY = "#1e1e2d"  
COLOR_BG_SECONDARY = "#2b2b3b" 
COLOR_ACCENT = "#3fb1f7"      
COLOR_TEXT_PRIMARY = "#dcdcdc"
COLOR_TEXT_EMPHASIS = "#ffffff"
COLOR_BORDER = "#3a3a4b"     
COLOR_GRAPH_TEAL = "#48c1a6"
COLOR_GRAPH_PINK = "#e66761"
 
class AvatarPlaceholder(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, width=50, height=50, corner_radius=25, border_width=1, border_color=COLOR_BORDER, fg_color=COLOR_BG_PRIMARY, **kwargs)
        self.pack_propagate(False)
        self.label = ctk.CTkLabel(self, text="U", font=("Segoe UI", 24, "bold"), text_color=COLOR_TEXT_PRIMARY)
        self.label.pack(expand=True)

class SummaryCard(ctk.CTkFrame):
    def __init__(self, master, title, initial_value, change_text="", chart_color=None, **kwargs):
        super().__init__(master, corner_radius=10, border_width=1, border_color=COLOR_BORDER, fg_color=COLOR_BG_SECONDARY, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0,1,2), weight=1)

        ctk.CTkLabel(self, text=title, font=("Segoe UI", 12), text_color=COLOR_TEXT_PRIMARY).grid(row=0, column=0, padx=15, pady=(15, 0), sticky="w")
        
        self.val_label = ctk.CTkLabel(self, text=initial_value, font=("Segoe UI", 32, "bold"), text_color=COLOR_TEXT_EMPHASIS)
        self.val_label.grid(row=1, column=0, padx=15, pady=0, sticky="w")
        
        bottom_frame = ctk.CTkFrame(self, fg_color="transparent", height=40)
        bottom_frame.grid(row=2, column=0, padx=15, pady=(0, 15), sticky="w")

        if change_text:
            ctk.CTkLabel(bottom_frame, text=change_text, font=("Segoe UI", 10), text_color="#888").pack(side="left")

        if chart_color:
            chart_placeholder = ctk.CTkFrame(self, width=80, height=20, corner_radius=10, fg_color=chart_color, border_width=0)
            chart_placeholder.place(relx=1.0, rely=1.0, anchor="se", x=-15, y=-15)

    def set_value(self, new_value):
        self.val_label.configure(text=new_value)

class RecentTransactions(ctk.CTkFrame):
    def __init__(self, master, engine, **kwargs):
        super().__init__(master, corner_radius=10, border_width=1, border_color=COLOR_BORDER, fg_color=COLOR_BG_SECONDARY, **kwargs)
        self.engine = engine
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        header_frame = ctk.CTkFrame(self, fg_color="transparent", height=40)
        header_frame.grid(row=0, column=0, sticky="ew", padx=15, pady=(15, 5))
        
        ctk.CTkLabel(header_frame, text="Recent Expenses", font=("Segoe UI", 16, "bold"), text_color=COLOR_TEXT_EMPHASIS).pack(side="left")

        utils_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        utils_frame.pack(side="right")

        export_btn = ctk.CTkButton(utils_frame, text="CSV ⬇", width=80, height=32, corner_radius=6, border_width=1, border_color=COLOR_BORDER, fg_color=COLOR_BG_PRIMARY, text_color=COLOR_TEXT_PRIMARY, font=("Segoe UI", 12), command=self.handle_export)
        export_btn.pack(side="right", padx=(5, 0))

        search_entry = ctk.CTkEntry(utils_frame, placeholder_text="Search category or desc...", width=200, height=32, corner_radius=6, border_width=1, border_color=COLOR_BORDER, fg_color=COLOR_BG_PRIMARY, text_color=COLOR_TEXT_PRIMARY)
        search_entry.pack(side="right")

        self.tree_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.tree_frame.grid(row=1, column=0, sticky="nsew", padx=15, pady=(0, 15))

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background=COLOR_BG_SECONDARY, foreground=COLOR_TEXT_PRIMARY, fieldbackground=COLOR_BG_SECONDARY, rowheight=35, font=("Segoe UI", 11), borderwidth=0)
        style.map("Treeview", background=[('selected', COLOR_ACCENT)])
        style.configure("Treeview.Heading", background=COLOR_BG_SECONDARY, foreground=COLOR_TEXT_EMPHASIS, font=("Segoe UI", 11, "bold"), borderwidth=0)
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])

        self.tree = ttk.Treeview(self.tree_frame, columns=("Date", "Category", "Description", "Amount"), show="headings", style="Treeview")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Description", text="Description")
        self.tree.heading("Amount", text="Amount")

        self.tree.column("Date", width=120, anchor="center")
        self.tree.column("Category", width=150, anchor="w")
        self.tree.column("Description", width=300, anchor="w")
        self.tree.column("Amount", width=100, anchor="center")

        self.tree.pack(fill="both", expand=True)

    def populate(self):
        # Clear existing rows
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # Fetch fresh data from engine
        data = self.engine.get_all_expenses()
        for row in data:
            formatted_amount = f"${row['amount']:.2f}"
            self.tree.insert("", "end", values=(row['date'], row['category'], row['description'], formatted_amount))

    def handle_export(self):
        success = self.engine.export_data()
        if success:
            messagebox.showinfo("Export Successful", "Data exported to export.csv successfully!")
        else:
            messagebox.showwarning("Export Failed", "No data available to export.")

class QuickAddExpense(ctk.CTkFrame):
    def __init__(self, master, engine, refresh_callback, **kwargs):
        super().__init__(master, corner_radius=10, border_width=1, border_color=COLOR_BORDER, fg_color=COLOR_BG_SECONDARY, **kwargs)
        self.engine = engine
        self.refresh_callback = refresh_callback
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0,1,2,3,4), weight=1)

        ctk.CTkLabel(self, text="Quick Add Expense", font=("Segoe UI", 16, "bold"), text_color=COLOR_TEXT_EMPHASIS).grid(row=0, column=0, padx=15, pady=(15, 10), sticky="w")

        self.amount_entry = ctk.CTkEntry(self, placeholder_text="Amount ($):", width=250, height=40, corner_radius=6, border_width=1, border_color=COLOR_BORDER, fg_color=COLOR_BG_PRIMARY, text_color=COLOR_TEXT_PRIMARY)
        self.amount_entry.grid(row=1, column=0, padx=15, pady=5, sticky="ew")

        self.category_entry = ctk.CTkEntry(self, placeholder_text="Category:", width=250, height=40, corner_radius=6, border_width=1, border_color=COLOR_BORDER, fg_color=COLOR_BG_PRIMARY, text_color=COLOR_TEXT_PRIMARY)
        self.category_entry.grid(row=2, column=0, padx=15, pady=5, sticky="ew")

        self.desc_entry = ctk.CTkEntry(self, placeholder_text="Description:", width=250, height=40, corner_radius=6, border_width=1, border_color=COLOR_BORDER, fg_color=COLOR_BG_PRIMARY, text_color=COLOR_TEXT_PRIMARY)
        self.desc_entry.grid(row=3, column=0, padx=15, pady=5, sticky="ew")

        add_btn = ctk.CTkButton(self, text="Add Expense +", font=("Segoe UI", 14, "bold"), corner_radius=6, border_width=0, fg_color=COLOR_ACCENT, text_color=COLOR_TEXT_EMPHASIS, height=40, command=self.submit_expense)
        add_btn.grid(row=4, column=0, padx=15, pady=(10, 15), sticky="ew")

    def submit_expense(self):
        amt = self.amount_entry.get()
        cat = self.category_entry.get()
        desc = self.desc_entry.get()
        
        success, message = self.engine.add_expense(amt, cat, desc)
        
        if success:
            # Clear fields
            self.amount_entry.delete(0, 'end')
            self.category_entry.delete(0, 'end')
            self.desc_entry.delete(0, 'end')
            # Tell master panel to refresh all dynamic data
            self.refresh_callback()
        else:
            messagebox.showerror("Input Error", message)

class DashboardSidebar(ctk.CTkFrame):
    def __init__(self, master, exit_callback, **kwargs):
        super().__init__(master, width=220, corner_radius=0, border_width=0, fg_color=COLOR_BG_SECONDARY, **kwargs)
        self.pack_propagate(False)

        ctk.CTkLabel(self, text="ExpenseTracker", font=("Segoe UI", 20, "bold"), text_color=COLOR_TEXT_EMPHASIS).pack(pady=(20, 20), anchor="w", padx=20)

        profile_frame = ctk.CTkFrame(self, fg_color="transparent")
        profile_frame.pack(pady=(0, 20), anchor="w", padx=20, fill="x")
        AvatarPlaceholder(profile_frame).pack(side="left")
        
        info_frame = ctk.CTkFrame(profile_frame, fg_color="transparent")
        info_frame.pack(side="left", padx=10)
        ctk.CTkLabel(info_frame, text="Nick Jenkins", font=("Segoe UI", 14, "bold"), text_color=COLOR_TEXT_EMPHASIS).pack(anchor="w")
        ctk.CTkLabel(info_frame, text="Pro Account", font=("Segoe UI", 10), text_color=COLOR_TEXT_PRIMARY).pack(anchor="w")

        nav_items = [("Dashboard", "□"), ("Transactions", "⇌"), ("Categories", "☊"), ("Balance", "⦿"), ("Settings", "⚙")]

        self.nav_buttons = []
        for text, icon in nav_items:
            btn = ctk.CTkButton(self, text=f" {icon}  {text}", font=("Segoe UI", 14), corner_radius=0, border_width=0, fg_color="transparent", text_color=COLOR_TEXT_PRIMARY, height=45, anchor="w", hover_color=COLOR_BORDER)
            btn.pack(fill="x", padx=10)
            self.nav_buttons.append(btn)
        
        self.nav_buttons[0].configure(fg_color=COLOR_ACCENT, text_color=COLOR_TEXT_EMPHASIS, font=("Segoe UI", 14, "bold"))

        ctk.CTkFrame(self, height=1, border_width=1, border_color=COLOR_BORDER, fg_color=COLOR_BORDER).pack(fill="x", pady=20, padx=20)

        system_frame = ctk.CTkFrame(self, fg_color="transparent")
        system_frame.pack(pady=(0, 10), side="bottom", fill="x", padx=10)

        ctk.CTkButton(system_frame, text="Light Mode □", width=90, height=32, corner_radius=6, border_width=1, border_color=COLOR_BORDER, fg_color=COLOR_BG_PRIMARY, text_color=COLOR_TEXT_PRIMARY, font=("Segoe UI", 11)).pack(side="left", padx=(0, 5))
        exit_btn = ctk.CTkButton(system_frame, text="Exit ⏼", width=90, height=32, corner_radius=6, border_width=0, fg_color="#c22f2f", text_color=COLOR_TEXT_EMPHASIS, font=("Segoe UI", 11, "bold"), command=exit_callback)
        exit_btn.pack(side="right")


class DashboardMainPanel(ctk.CTkFrame):
    def __init__(self, master, engine, **kwargs):
        super().__init__(master, corner_radius=0, border_width=0, fg_color=COLOR_BG_PRIMARY, **kwargs)
        self.engine = engine
        
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0,1,2), weight=1)

        header_frame = ctk.CTkFrame(self, fg_color="transparent", height=50)
        header_frame.grid(row=0, column=0, columnspan=2, sticky="ew", padx=30, pady=(25, 10))
        ctk.CTkLabel(header_frame, text="My Dashboard", font=("Segoe UI", 24, "bold"), text_color=COLOR_TEXT_EMPHASIS).pack(side="left")

        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        month_picker = ctk.CTkOptionMenu(header_frame, values=months, width=120, corner_radius=8, fg_color=COLOR_BG_SECONDARY, button_color=COLOR_BG_SECONDARY, button_hover_color=COLOR_BORDER, dropdown_fg_color=COLOR_BG_SECONDARY, dropdown_hover_color=COLOR_BORDER, dropdown_text_color=COLOR_TEXT_PRIMARY, text_color=COLOR_TEXT_PRIMARY, font=("Segoe UI", 12))
        month_picker.pack(side="right", padx=(10, 0))
        month_picker.set(months[date.today().month - 1])

        # Grid Components
        QuickAddExpense(self, engine=self.engine, refresh_callback=self.refresh_ui).grid(row=1, column=0, padx=30, pady=20, sticky="nsew")

        summary_cards_frame = ctk.CTkFrame(self, fg_color="transparent")
        summary_cards_frame.grid(row=1, column=1, padx=(0, 30), pady=20, sticky="nsew")
        summary_cards_frame.grid_columnconfigure((0,1), weight=1)
        summary_cards_frame.grid_rowconfigure(0, weight=1)

        self.total_card = SummaryCard(summary_cards_frame, title="Total Balance", initial_value="$0.00")
        self.total_card.grid(row=0, column=0, padx=10, sticky="nsew")
        
        self.month_card = SummaryCard(summary_cards_frame, title="This Month Expense", initial_value="$0.00", chart_color=COLOR_GRAPH_PINK)
        self.month_card.grid(row=0, column=1, padx=10, sticky="nsew")

        self.ledger = RecentTransactions(self, engine=self.engine)
        self.ledger.grid(row=2, column=0, columnspan=2, padx=30, pady=(10, 30), sticky="nsew")
        
        # Initial Population
        self.refresh_ui()

    def refresh_ui(self):
        """Pulls fresh calculations from engine and updates UI elements."""
        total = self.engine.get_total_balance()
        month_total = self.engine.get_current_month_total()
        
        self.total_card.set_value(f"${total:,.2f}")
        self.month_card.set_value(f"${month_total:,.2f}")
        self.ledger.populate()


class ExpenseTrackerApp(ctk.CTk):
    def __init__(self, engine):
        super().__init__()
        
        self.title("ExpenseTracker - Modern Dashboard")
        self.geometry("1100x700")
        self.resizable(False, False)
        self.configure(fg_color=COLOR_BG_PRIMARY)

        self.grid_columnconfigure(0, weight=0) 
        self.grid_columnconfigure(1, weight=1) 
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = DashboardSidebar(self, exit_callback=self.quit_app)
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        self.main_panel = DashboardMainPanel(self, engine=engine)
        self.main_panel.grid(row=0, column=1, sticky="nsew")

    def quit_app(self):
        self.destroy()