import tkinter as tk
from tkinter import ttk, messagebox
import random
import datetime

# Simple fraud detection class
class FraudDetector:
    def __init__(self):
        self.history = []
    
    def check_fraud(self, amount, country, hour, merchant, prev_transactions):
        # Simple rule-based fraud detection
        risk_score = 0
        reasons = []
        
        # Check amount
        if amount > 5000:
            risk_score += 40
            reasons.append("Very high amount")
        elif amount > 1000:
            risk_score += 20
            reasons.append("High amount")
        
        # Check country
        if country.lower() not in ['usa', 'united states', 'us']:
            risk_score += 30
            reasons.append("Foreign country")
        
        # Check time
        if hour < 6 or hour > 22:
            risk_score += 25
            reasons.append("Unusual time")
        
        # Check merchant
        if merchant == "Online" and amount > 500:
            risk_score += 15
            reasons.append("High online purchase")
        
        # Check frequency
        if prev_transactions > 8:
            risk_score += 30
            reasons.append("Too many transactions")
        
        # Add some randomness
        risk_score += random.randint(0, 10)
        
        is_fraud = risk_score > 50
        return is_fraud, min(risk_score, 100), reasons

class FraudDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Credit Card Fraud Detection System")
        self.root.geometry("600x700")
        self.root.configure(bg='lightblue')
        
        # Create detector
        self.detector = FraudDetector()
        
        # Create GUI elements
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="🛡️ Credit Card Fraud Detection", 
                              font=('Arial', 16, 'bold'), bg='lightblue', fg='darkblue')
        title_label.pack(pady=10)
        
        # Main frame
        main_frame = tk.Frame(self.root, bg='white', relief='raised', bd=2)
        main_frame.pack(padx=20, pady=10, fill='both', expand=True)
        
        # Input fields frame
        input_frame = tk.LabelFrame(main_frame, text="Transaction Details", 
                                   font=('Arial', 12, 'bold'), bg='white')
        input_frame.pack(padx=10, pady=10, fill='x')
        
        # Card number
        tk.Label(input_frame, text="Card Number (last 4 digits):", bg='white').pack(anchor='w', padx=10, pady=2)
        self.card_entry = tk.Entry(input_frame, width=30)
        self.card_entry.pack(padx=10, pady=2)
        
        # Amount
        tk.Label(input_frame, text="Amount ($):", bg='white').pack(anchor='w', padx=10, pady=2)
        self.amount_entry = tk.Entry(input_frame, width=30)
        self.amount_entry.pack(padx=10, pady=2)
        
        # Country
        tk.Label(input_frame, text="Country:", bg='white').pack(anchor='w', padx=10, pady=2)
        self.country_entry = tk.Entry(input_frame, width=30)
        self.country_entry.pack(padx=10, pady=2)
        
        # City
        tk.Label(input_frame, text="City:", bg='white').pack(anchor='w', padx=10, pady=2)
        self.city_entry = tk.Entry(input_frame, width=30)
        self.city_entry.pack(padx=10, pady=2)
        
        # Merchant type
        tk.Label(input_frame, text="Merchant Type:", bg='white').pack(anchor='w', padx=10, pady=2)
        self.merchant_var = tk.StringVar()
        merchant_combo = ttk.Combobox(input_frame, textvariable=self.merchant_var, width=28)
        merchant_combo['values'] = ('Grocery', 'Gas Station', 'Restaurant', 'Online', 'ATM', 'Other')
        merchant_combo.pack(padx=10, pady=2)
        
        # Time
        tk.Label(input_frame, text="Hour (0-23):", bg='white').pack(anchor='w', padx=10, pady=2)
        self.time_entry = tk.Entry(input_frame, width=30)
        self.time_entry.pack(padx=10, pady=2)
        
        # Previous transactions
        tk.Label(input_frame, text="Previous transactions today:", bg='white').pack(anchor='w', padx=10, pady=2)
        self.prev_tx_entry = tk.Entry(input_frame, width=30)
        self.prev_tx_entry.pack(padx=10, pady=2)
        
        # Buttons frame
        button_frame = tk.Frame(input_frame, bg='white')
        button_frame.pack(pady=10)
        
        # Analyze button
        analyze_btn = tk.Button(button_frame, text="Analyze Transaction", 
                               command=self.analyze_transaction, bg='darkblue', fg='white',
                               font=('Arial', 12, 'bold'), width=15)
        analyze_btn.pack(side='left', padx=5)
        
        # Sample data buttons
        normal_btn = tk.Button(button_frame, text="Load Normal", 
                              command=self.load_normal_sample, bg='green', fg='white')
        normal_btn.pack(side='left', padx=5)
        
        fraud_btn = tk.Button(button_frame, text="Load Suspicious", 
                             command=self.load_fraud_sample, bg='red', fg='white')
        fraud_btn.pack(side='left', padx=5)
        
        # Clear button
        clear_btn = tk.Button(button_frame, text="Clear", 
                             command=self.clear_fields, bg='gray', fg='white')
        clear_btn.pack(side='left', padx=5)
        
        # Results frame
        self.result_frame = tk.LabelFrame(main_frame, text="Analysis Results", 
                                         font=('Arial', 12, 'bold'), bg='white')
        self.result_frame.pack(padx=10, pady=10, fill='both', expand=True)
        
        # Result text
        self.result_text = tk.Text(self.result_frame, height=15, width=50, 
                                  font=('Arial', 10), bg='lightyellow')
        self.result_text.pack(padx=10, pady=10, fill='both', expand=True)
        
        # Scrollbar for result text
        scrollbar = tk.Scrollbar(self.result_frame, command=self.result_text.yview)
        self.result_text.configure(yscrollcommand=scrollbar.set)
    
    def analyze_transaction(self):
        try:
            # Get input values
            card_num = self.card_entry.get()
            amount = float(self.amount_entry.get())
            country = self.country_entry.get()
            city = self.city_entry.get()
            merchant = self.merchant_var.get()
            hour = int(self.time_entry.get())
            prev_tx = int(self.prev_tx_entry.get())
            
            # Validate inputs
            if not all([card_num, amount, country, city, merchant]):
                messagebox.showerror("Error", "Please fill all fields!")
                return
            
            if hour < 0 or hour > 23:
                messagebox.showerror("Error", "Hour must be between 0-23!")
                return
            
            # Analyze transaction
            is_fraud, risk_score, reasons = self.detector.check_fraud(
                amount, country, hour, merchant, prev_tx
            )
            
            # Display results
            self.display_results(is_fraud, risk_score, reasons, 
                               card_num, amount, country, city, merchant, hour)
            
            # Save to history
            transaction = {
                'card': card_num,
                'amount': amount,
                'merchant': merchant,
                'is_fraud': is_fraud,
                'time': datetime.datetime.now().strftime("%H:%M:%S")
            }
            self.detector.history.append(transaction)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for amount, hour, and previous transactions!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def display_results(self, is_fraud, risk_score, reasons, card_num, amount, country, city, merchant, hour):
        self.result_text.delete(1.0, tk.END)
        
        # Header
        self.result_text.insert(tk.END, "="*50 + "\n")
        self.result_text.insert(tk.END, "FRAUD DETECTION ANALYSIS RESULTS\n")
        self.result_text.insert(tk.END, "="*50 + "\n\n")
        
        # Transaction details
        self.result_text.insert(tk.END, "Transaction Details:\n")
        self.result_text.insert(tk.END, f"Card: ****{card_num}\n")
        self.result_text.insert(tk.END, f"Amount: ${amount:.2f}\n")
        self.result_text.insert(tk.END, f"Location: {city}, {country}\n")
        self.result_text.insert(tk.END, f"Merchant: {merchant}\n")
        self.result_text.insert(tk.END, f"Time: {hour}:00\n\n")
        
        # Results
        if is_fraud:
            self.result_text.insert(tk.END, "🚨 FRAUD ALERT! 🚨\n", 'fraud')
            self.result_text.insert(tk.END, "This transaction is SUSPICIOUS!\n\n")
        else:
            self.result_text.insert(tk.END, "✅ SAFE TRANSACTION ✅\n", 'safe')
            self.result_text.insert(tk.END, "This transaction appears normal.\n\n")
        
        # Risk score
        self.result_text.insert(tk.END, f"Risk Score: {risk_score}%\n")
        
        # Risk level
        if risk_score > 70:
            risk_level = "HIGH"
        elif risk_score > 40:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"
        self.result_text.insert(tk.END, f"Risk Level: {risk_level}\n\n")
        
        # Reasons
        if reasons:
            self.result_text.insert(tk.END, "Suspicious factors found:\n")
            for i, reason in enumerate(reasons, 1):
                self.result_text.insert(tk.END, f"{i}. {reason}\n")
        else:
            self.result_text.insert(tk.END, "No suspicious factors detected.\n")
        
        self.result_text.insert(tk.END, "\n")
        
        # History
        if self.detector.history:
            self.result_text.insert(tk.END, "-"*30 + "\n")
            self.result_text.insert(tk.END, "RECENT TRANSACTIONS:\n")
            self.result_text.insert(tk.END, "-"*30 + "\n")
            
            for tx in self.detector.history[-5:]:  # Show last 5
                status = "FRAUD" if tx['is_fraud'] else "SAFE"
                self.result_text.insert(tk.END, 
                    f"${tx['amount']:.2f} - {tx['merchant']} - {status} ({tx['time']})\n")
        
        # Configure text colors
        self.result_text.tag_configure('fraud', foreground='red', font=('Arial', 12, 'bold'))
        self.result_text.tag_configure('safe', foreground='green', font=('Arial', 12, 'bold'))
    
    def load_normal_sample(self):
        """Load a normal transaction example"""
        self.card_entry.delete(0, tk.END)
        self.card_entry.insert(0, "1234")
        
        self.amount_entry.delete(0, tk.END)
        self.amount_entry.insert(0, "45.99")
        
        self.country_entry.delete(0, tk.END)
        self.country_entry.insert(0, "USA")
        
        self.city_entry.delete(0, tk.END)
        self.city_entry.insert(0, "New York")
        
        self.merchant_var.set("Grocery")
        
        self.time_entry.delete(0, tk.END)
        self.time_entry.insert(0, "14")
        
        self.prev_tx_entry.delete(0, tk.END)
        self.prev_tx_entry.insert(0, "3")
    
    def load_fraud_sample(self):
        """Load a suspicious transaction example"""
        self.card_entry.delete(0, tk.END)
        self.card_entry.insert(0, "9876")
        
        self.amount_entry.delete(0, tk.END)
        self.amount_entry.insert(0, "7500.00")
        
        self.country_entry.delete(0, tk.END)
        self.country_entry.insert(0, "Nigeria")
        
        self.city_entry.delete(0, tk.END)
        self.city_entry.insert(0, "Lagos")
        
        self.merchant_var.set("Online")
        
        self.time_entry.delete(0, tk.END)
        self.time_entry.insert(0, "3")
        
        self.prev_tx_entry.delete(0, tk.END)
        self.prev_tx_entry.insert(0, "15")
    
    def clear_fields(self):
        """Clear all input fields"""
        self.card_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.country_entry.delete(0, tk.END)
        self.city_entry.delete(0, tk.END)
        self.merchant_var.set("")
        self.time_entry.delete(0, tk.END)
        self.prev_tx_entry.delete(0, tk.END)
        self.result_text.delete(1.0, tk.END)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = FraudDetectionApp(root)
    root.mainloop()