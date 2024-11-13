from django.shortcuts import render,redirect
from datetime import datetime
import os
from .models import EasyDumps,File 

def home(request):
    if request.method == "POST":
        file = request.FILES['file']
        obj = File.objects.create(file=file)
        save_sftp(obj.file.path)
        #redirect('succesful')
    return render(request, "home.html", {})

def succesful(request):
    render(request, "succesful.html")
# Create your views here.
def save_sftp(file_path):
    
    records_saved = 0
    if not os.path.isfile(file_path):
        print("File not found.")
        return None

    try:
        with open(file_path, 'rb') as file:
            lines = file.read().decode('utf-8', errors='replace').splitlines()
            
            sof_info = ""
            terminal_id = date = time = None
            amount = transaction_fee = easy_ref = None
            paid_amount = bank_cost = payment_type = None

            for line in lines:
                parts = line.split(',')
                line_type = parts[0].strip()

                if line_type == "SOF":
                    sof_info = line.strip()

                elif line_type == "X":
                    terminal_id = parts[1].strip()
                    date = parts[2].strip()
                    time = parts[3].strip()

                elif line_type == "P":
                    amount = float(parts[1].strip())
                    transaction_fee = float(parts[2].strip())
                    easy_ref = parts[3].strip()

                elif line_type == "T":
                    paid_amount = float(parts[1].strip())
                    bank_cost = float(parts[2].strip())
                    payment_type = parts[3].strip()

                    date_obj = datetime.strptime(date, "%Y%m%d").date() if date else None

                    easy_dump = EasyDumps(
                        terminal_id=terminal_id,
                        time=time,
                        date=date_obj,
                        amount=amount,
                        transaction_fee=transaction_fee,
                        easy_ref=easy_ref,
                        payment_type=payment_type,
                        paid_amount=paid_amount,
                        bank_cost=bank_cost,
                        sof_info=sof_info
                    )
                    easy_dump.save()
                    records_saved += 1

        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File {file_path} has been deleted successfully.")
    except Exception as e:
        print(f"Error reading file: {e}")

    print(f"Total records saved: {records_saved}")
    return records_saved