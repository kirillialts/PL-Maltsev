import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
from datetime import datetime

class GitHubRepoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GitHub Repository Info")
        self.root.geometry("600x400")
        
        self.create_widgets()
    
    def create_widgets(self):
        
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        
        title_label = ttk.Label(main_frame, text="GitHub Repository Information", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        
        ttk.Label(main_frame, text="Repository Name:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.repo_entry = ttk.Entry(main_frame, width=40)
        self.repo_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        self.repo_entry.bind('<Return>', lambda e: self.get_repo_info())
        
        
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=20)
        
        self.get_info_btn = ttk.Button(button_frame, text="Get Repository Info", 
                                      command=self.get_repo_info)
        self.get_info_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.clear_btn = ttk.Button(button_frame, text="Clear", 
                                   command=self.clear_fields)
        self.clear_btn.pack(side=tk.LEFT)
        
       
        results_frame = ttk.LabelFrame(main_frame, text="Repository Information", padding="10")
        results_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        
        
        self.results_text = tk.Text(results_frame, height=15, width=70, wrap=tk.WORD)
        scrollbar = ttk.Scrollbar(results_frame, orient=tk.VERTICAL, command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scrollbar.set)
        
        self.results_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(3, weight=1)
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)
    
    def get_repo_info(self):
        repo_name = self.repo_entry.get().strip()
        
        if not repo_name:
            messagebox.showerror("Error", "Please enter a repository name")
            return
        
        try:
            url = f"https://api.github.com/repos/{repo_name}"
            
            response = requests.get(url)
            
            if response.status_code == 200:
                repo_data = response.json()
                
                
                owner_info = repo_data.get('owner', {})
                
                result_data = {
                    'company': owner_info.get('company'),
                    'created_at': owner_info.get('created_at'),
                    'email': owner_info.get('email'),
                    'id': owner_info.get('id'),
                    'name': owner_info.get('login'),
                    'url': owner_info.get('url')
                }
                
                
                self.results_text.delete(1.0, tk.END)
                formatted_json = json.dumps(result_data, indent=2, ensure_ascii=False)
                self.results_text.insert(1.0, formatted_json)
                
                
                self.save_to_file(result_data, repo_name)
                
                messagebox.showinfo("Success", f"Information saved to {repo_name}_info.json")
                
            elif response.status_code == 404:
                messagebox.showerror("Error", "Repository not found")
            else:
                messagebox.showerror("Error", f"API Error: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Network error: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {str(e)}")
    
    def save_to_file(self, data, repo_name):
        filename = f"{repo_name.replace('/', '_')}_info.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def clear_fields(self):
        self.repo_entry.delete(0, tk.END)
        self.results_text.delete(1.0, tk.END)

def main():
    root = tk.Tk()
    app = GitHubRepoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()